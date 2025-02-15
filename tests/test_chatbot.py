import sys
import os

# Ensure the project root is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

# Import the Chatbot class
from backend.chatbot import Chatbot

# Initialize the chatbot
chatbot = Chatbot()

# Test input
query = "What is artificial intelligence?"

# Get chatbot response
response = chatbot.get_response(query)

# Print the chatbot's response
print("\n🧠 Chatbot Response:")
print(response)