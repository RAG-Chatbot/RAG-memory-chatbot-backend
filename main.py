## main.py
from backend.chatbot import Chatbot

chatbot = Chatbot()

print("\n🔹 Lifetime Memory Chatbot (Type 'exit' to quit, 'clear memory' to reset) 🔹\n")

while True:
    query = input("👤 You: ")
    
    if query.lower() == "exit":
        print("🚀 Chatbot shutting down... Goodbye!")
        break

    if query.lower() == "clear memory":
        print("🤖 AI:", chatbot.memory.clear_memory())  # ✅ Ensures memory is wiped properly
        continue

    response = chatbot.get_response(query)
    print(f"🤖 AI: {response}\n")