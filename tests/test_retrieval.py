import sys
import os

# Get the absolute path of the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)  # Add project root to sys.path

# Now import the module correctly
from backend.retrieval import RAGRetriever

retriever = RAGRetriever()
response = retriever.retrieve_memory("Tell me about AI")
print("Retrieved Memory:", response)