import sys
import os

# Add the parent directory (project root) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.memory_manager import MemoryManager

# Initialize memory manager
memory = MemoryManager()

# Store an interaction
memory.store_interaction("What is AI?", "AI is a branch of computer science.")

# Retrieve stored interactions
print(memory.collection.get())  # Should return stored interactions