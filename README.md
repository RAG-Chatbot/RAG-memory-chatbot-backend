Here’s an updated README.md with a clear and structured explanation of the backend approach and step-by-step process of how the chatbot works.

RAG-Based Lifetime Memory Chatbot

🚀 An AI Chatbot with Retrieval-Augmented Generation (RAG), Lifetime Memory, and Web Search Capabilities

📌 Overview

The Lifetime Memory Chatbot is an advanced Retrieval-Augmented Generation (RAG) chatbot that:
✅ Remembers past interactions and recalls relevant memory.
✅ Retrieves relevant information using FAISS-based vector similarity search.
✅ Enhances responses using pre-trained language models (FLAN-T5).
✅ Fetches live data via DuckDuckGo Web Search when memory is insufficient.
✅ Provides a web-based interface for users to interact with the chatbot.

🎯 Project Approach

How Does the Backend Work?

This chatbot uses Retrieval-Augmented Generation (RAG) to generate responses intelligently by combining stored memory and external search capabilities. Below is the detailed approach:

Step-by-Step Execution Process

1️⃣ User Inputs Query
	•	The user enters a question or statement in the chatbot interface (CLI or Web UI).
	•	The backend receives the query and processes it.

2️⃣ Checking for User Identity
	•	If the user says, “My name is X”, the chatbot remembers and stores the name.
	•	If the user asks, “What is my name?”, it retrieves the name from memory.

3️⃣ Memory Retrieval (Long-Term & Short-Term Memory)
	•	The chatbot first checks past conversations in short-term memory (STM) (last 10 interactions).
	•	If no relevant match is found, it queries long-term memory (LTM) stored in ChromaDB.
	•	It uses FAISS (Facebook AI Similarity Search) to find the most relevant past interactions.

4️⃣ Generating a Response
	•	If relevant memory is found, it uses the retrieved context to generate a response.
	•	If no relevant memory exists, it tries web search using DuckDuckGo API.
	•	The chatbot then constructs a prompt including memory or search results.
	•	The FLAN-T5 (google/flan-t5-large) model processes the query and generates a coherent response.

5️⃣ Storing the Conversation in Memory
	•	After generating a response, it stores the user query and AI response in memory.
	•	New interactions get added to STM and LTM (ChromaDB storage).

6️⃣ Displaying the Response
	•	The chatbot prints the response in CLI (Terminal) and Web UI (Chat Interface).
	•	Users can continue chatting, and the chatbot remembers context for future queries.

🛠 Project Structure

Lifetime-Memory-Chatbot
│── backend/
│   │── chatbot.py           # Main chatbot logic (RAG + Web Search)
│   │── memory_manager.py    # Handles STM, LTM & User Profile
│   │── retrieval.py         # FAISS-based vector retrieval
│   │── database.py          # Empty (can be used for DB expansion)
│   │── config.py            # Empty (for future configurations)
│   └── __init__.py          # Required for module import
|
│── tests/
│   │── test_chatbot.py      # Unit test for chatbot response
│   │── test_memory.py       # Unit test for memory storage
│   │── test_retrieval.py    # Unit test for FAISS-based retrieval
│
│── main.py                  # Runs chatbot in CLI
│── .gitignore                # Ignore unnecessary files
│── readme.md                 # Project Documentation
│── requirements.txt          # Dependencies
└── faiss_index.bin           # FAISS Vector Store (Auto-Generated)

🔬 Detailed Explanation of Backend Components

1️⃣ chatbot.py (Main Logic)
	•	Handles user queries and manages the complete response generation workflow.
	•	Checks user identity and remembers the name.
	•	Queries past memory or searches the web if memory is insufficient.
	•	Uses FLAN-T5 to generate responses based on retrieved information.

2️⃣ memory_manager.py (Memory Handling)
	•	Manages Short-Term Memory (STM) (last 10 interactions).
	•	Stores Long-Term Memory (LTM) in ChromaDB.
	•	Handles name retention when a user introduces themselves.

3️⃣ retrieval.py (RAG Retrieval)
	•	Uses FAISS to perform vector-based similarity searches.
	•	Retrieves contextually relevant responses from long-term memory.
	•	Ensures memory relevance before passing it to the chatbot.

4️⃣ DuckDuckGo Web Search
	•	When memory does not contain relevant answers, the chatbot searches the web.
	•	Integrates DuckDuckGo API to fetch live search results.

🛠 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/RAG-Chatbot/RAG-memory-chatbot-backend.git
cd RAG-memory-chatbot-backend

2️⃣ Create & Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Chatbot

To run in CLI mode, use:

python main.py

To run the Frontend Web UI:

cd frontend
python -m http.server 8080

Then, open http://127.0.0.1:8080 in your browser.

📢 Usage

💬 Interacting with the Chatbot

Once started, you can ask questions like:

👤 You: My name is Anarv.
🤖 AI: Got it! I'll remember your name as Anarv.

👤 You: What is my name?
🤖 AI: Your name is Anarv.

👤 You: What is Blockchain?
🤖 AI: (Retrieves from memory OR searches online if needed)

👤 You: clear memory
🤖 AI: 🧹 Memory Cleared: All past interactions erased.

🎯 Future Improvements

🔹 Multi-User Support: Extend memory storage for multiple users.
🔹 Customizable API Integration: Allow switching between multiple search engines.
🔹 Better RAG Optimization: Improve FAISS-based search accuracy.
🔹 GUI Enhancements: Advanced chat UI with better user experience.

🔥 Contributing
	1.	Fork the repo
	2.	Create a feature branch: git checkout -b feature-xyz
	3.	Commit changes: git commit -m "Added XYZ feature"
	4.	Push & Submit PR: git push origin feature-xyz


This step-by-step breakdown ensures that the jury (or anyone) can easily understand how the chatbot is built and operates. 🚀 Let me know if you need further clarifications or modifications!
