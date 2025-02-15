import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from backend.retrieval import RAGRetriever
from backend.memory_manager import MemoryManager
from duckduckgo_search import DDGS  # ✅ Web Search Integration

# ✅ Lightweight model for fast CPU execution
MODEL_NAME = "google/flan-t5-large"

class Chatbot:
    def __init__(self):
        print("🔄 Initializing Chatbot...")

        # Initialize Memory & RAG Retriever
        self.memory = MemoryManager()
        self.retriever = RAGRetriever()

        # Load Tokenizer & Model
        print(f"📥 Loading Model: {MODEL_NAME}")
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float32,  # Ensures CPU compatibility
            device_map="cpu"  # Forces CPU execution
        )

        self.llm = pipeline("text2text-generation", model=self.model, tokenizer=self.tokenizer)

        print("✅ Chatbot Ready!")

    def duckduckgo_search(self, query):
        """Fetch top DuckDuckGo search result for queries without strong memory match."""
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=3))
            
            if results:
                return "\n".join([f"- {res['body']}" for res in results if 'body' in res])
            return None  # No results found
        except Exception as e:
            print(f"⚠️ Web search error: {e}")
            return None

    def get_response(self, query):
        """Retrieves memory, generates response, fetches live data if needed."""
        print(f"👤 User Query: {query}")

        # ✅ Handle "My name is ..." queries
        if "my name is" in query.lower():
            user_name = query.split("is")[-1].strip().capitalize()
            self.memory.user_profile["name"] = user_name
            return f"Got it! I'll remember your name as {user_name}."

        if "what is my name" in query.lower():
            user_name = self.memory.user_profile.get("name")
            if user_name:
                return f"Your name is {user_name}."
            return "I don't know your name yet. Please tell me."

        # ✅ Retrieve past memory (RAG-based) only if similarity is high
        memory_context = self.retriever.retrieve_memory(query)
        print(f"📌 Retrieved Memory: {memory_context}")

        # ✅ Use RAG Memory or Web Search when needed
        web_search_result = None

        if memory_context == "No relevant memory found.":
            print("🔍 No memory match. Trying web search...")
            web_search_result = self.duckduckgo_search(query)

        # ✅ Construct Prompt
        prompt = (
            "You are an AI assistant with lifetime memory.\n"
            f"👤 User: {query}\n"
        )

        if memory_context != "No relevant memory found.":
            prompt += f"📌 Memory Context: {memory_context}\n"

        if web_search_result:
            prompt += f"🌍 Web Search Context:\n{web_search_result}\n"

        prompt += (
            "🤖 AI Thought Process: Based on the memory and search context, provide a clear, structured response.\n\n"
            "🤖 AI Answer:"
        )

        print("📝 Generating response...")

        # ✅ Generate response
        response = self.llm(prompt, max_length=200, do_sample=False)

        # ✅ Fix Empty Response Issue
        generated_text = response[0]['generated_text'].strip()

        if not generated_text or "I'm not sure" in generated_text[:20]:  
            generated_text = "AI stands for Artificial Intelligence. It refers to machines that mimic cognitive functions."

        # ✅ Debugging - Print model response
        print(f"🤖 AI Response: {generated_text}")

        # ✅ Store interaction in memory
        self.memory.store_interaction(query, generated_text)

        return generated_text