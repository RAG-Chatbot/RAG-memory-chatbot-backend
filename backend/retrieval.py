import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from backend.memory_manager import MemoryManager

class RAGRetriever:
    def __init__(self):
        self.memory = MemoryManager()
        self.embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.index_path = "faiss_index.bin"

        # ✅ Ensure FAISS index loads properly
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            self.index = faiss.IndexFlatL2(384)  # 384 is the embedding dimension

    def retrieve_memory(self, query):
        """Retrieve only relevant past conversations using FAISS similarity search."""

        # ✅ FIXED: Prioritize User Name Retrieval
        if "what is my name" in query.lower():
            stored_name = self.memory.user_profile.get("name")
            return stored_name if stored_name else "I don't know your name yet. Please tell me."

        stored_data = self.memory.collection.get()

        if not stored_data["documents"]:
            return "No relevant memory found."

        # ✅ Embed query
        query_vector = self.embedding_model.encode(query).reshape(1, -1)

        # ✅ Embed stored conversations
        stored_vectors = np.array([self.embedding_model.encode(doc) for doc in stored_data["documents"]])

        # ✅ FIX: Ensure stored vectors are not empty
        if stored_vectors.size == 0:
            return "No relevant memory found."

        # ✅ Add to FAISS index if not already added
        if self.index.ntotal == 0:
            self.index.add(stored_vectors)
            faiss.write_index(self.index, self.index_path)  # Save FAISS index

        # ✅ Search in FAISS for most relevant memory
        D, I = self.index.search(query_vector, k=3)  # Retrieve top 3 memories
        relevant_memories = [stored_data["documents"][i] for i in I[0] if i >= 0]

        # ✅ Ensure retrieved memory is actually related to the query
        best_memory = next((mem for mem in relevant_memories if self._is_relevant(mem, query)), "No relevant memory found.")

        return best_memory

    def _is_relevant(self, memory, query):
        """Check if retrieved memory is actually relevant to the current query."""
        return any(word in memory.lower() for word in query.lower().split())