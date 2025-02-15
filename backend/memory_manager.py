import chromadb
import uuid

class MemoryManager:
    def __init__(self):
        self.stm = []  # Short-Term Memory (recent 10 queries)
        self.chroma_client = chromadb.PersistentClient(path="memory_db")
        self.collection = self.chroma_client.get_or_create_collection(name="long_term_memory")

        # ✅ FIXED: Store User Profile Separately
        self.user_profile = {"name": None}  # Store the user's name properly

    def store_interaction(self, query, response):
        """Stores conversations while handling personal user details correctly."""
        
        # ✅ NEW: Properly Detect & Store User Name
        if "my name is" in query.lower():
            name = query.split("my name is")[-1].strip().split(".")[0].capitalize()
            self.user_profile["name"] = name  # Store only the extracted name
            print(f"📝 Remembering User Name: {name}")
            return f"Got it! I'll remember your name, {name}."

        # ✅ Maintain recent 10 interactions in STM
        if len(self.stm) > 10:
            self.stm.pop(0)
        self.stm.append({"query": query, "response": response})

        # ✅ Store in Long-Term Memory
        if query.lower() not in ["hi", "hello", "thanks", "bye", "exit", "clear memory"]:
            doc_id = str(uuid.uuid4())
            self.collection.add(
                documents=[query],
                metadatas=[{"response": response}],
                ids=[doc_id]
            )

    def retrieve_memory(self, query):
        """Retrieves stored memory, prioritizing personal user information first."""
        
        # ✅ FIXED: Retrieve User Name Correctly
        if "what is my name" in query.lower():
            stored_name = self.user_profile.get("name")
            return stored_name if stored_name else "I don't know your name yet. Please tell me."

        stored_data = self.collection.get()

        if not stored_data["documents"]:
            return "No relevant memory found."

        # ✅ FIXED: Prevent wrong memory retrieval (ensuring relevance)
        for i, stored_query in enumerate(stored_data["documents"]):
            if stored_query.lower() in query.lower() or query.lower() in stored_query.lower():
                return stored_data["metadatas"][i]["response"]

        return "No relevant memory found."

    def clear_memory(self):
        """Completely wipes all stored memories (STM + LTM) and resets user profile."""
        self.stm.clear()
        
        # ✅ FIX: Delete all stored IDs
        all_ids = self.collection.get()["ids"]
        if all_ids:
            self.collection.delete(ids=all_ids)

        # ✅ FIX: Reset User Profile
        self.user_profile = {"name": None}

        return "🧹 Memory Cleared: All past interactions erased."