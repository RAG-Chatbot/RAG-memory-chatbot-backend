# 🚀 RAG-Based Lifetime Memory Chatbot

An AI Chatbot with Retrieval-Augmented Generation (RAG), Lifetime Memory, and Web Search Capabilities.

---

## 📌 Overview  

The **Lifetime Memory Chatbot** is an advanced **Retrieval-Augmented Generation (RAG)** chatbot that:  

✅ **Remembers past interactions** and recalls relevant memory.  
✅ **Retrieves relevant information** using **FAISS-based vector similarity search**.  
✅ **Enhances responses** using **pre-trained language models (FLAN-T5)**.  
✅ **Fetches live data** via **DuckDuckGo Web Search** when memory is insufficient.  
✅ **Provides a web-based interface** for users to interact with the chatbot.  

---

## 🎯 Project Approach  

### **How Does the Backend Work?**  
This chatbot **combines memory storage and retrieval with real-time web search** to generate intelligent responses.  
It uses **RAG (Retrieval-Augmented Generation)** for response generation by leveraging **stored memory and live search results**.

---

## 🚀 Step-by-Step Execution Process  

### **1️⃣ User Inputs Query**  
- The **user enters a question** or **statement** via **CLI (Terminal)** or **Web UI**.  
- The **backend receives the query** and processes it.

### **2️⃣ Checking for User Identity**  
- If the user says, **"My name is X"**, the chatbot **remembers and stores the name**.  
- If the user asks, **"What is my name?"**, it **retrieves the name from memory**.

### **3️⃣ Memory Retrieval (Long-Term & Short-Term Memory)**  
- The chatbot first **checks past conversations** in **Short-Term Memory (STM)** (**last 10 interactions**).  
- If **no relevant match** is found, it **queries Long-Term Memory (LTM)** stored in **ChromaDB**.  
- It uses **FAISS (Facebook AI Similarity Search)** to **find the most relevant past interactions**.

### **4️⃣ Generating a Response**  
- If **relevant memory** is found, it **uses the retrieved context** to generate a response.  
- If **no relevant memory exists**, it **tries web search** using **DuckDuckGo API**.  
- The chatbot then **constructs a prompt** including **memory or search results**.  
- The **FLAN-T5 (google/flan-t5-large)** model **processes the query** and generates a coherent response.

### **5️⃣ Storing the Conversation in Memory**  
- After generating a response, it **stores the user query and AI response** in memory.  
- New interactions get **added to STM and LTM** (**ChromaDB storage**).

### **6️⃣ Displaying the Response**  
- The chatbot **prints the response** in **CLI (Terminal)** and **Web UI (Chat Interface)**.  
- Users can **continue chatting**, and the chatbot **remembers context** for future queries.

---

## 🛠 Project Structure  

```
Lifetime-Memory-Chatbot/
│── backend/  
│   │── chatbot.py         # Main chatbot logic (RAG + Web Search)  
│   │── memory_manager.py  # Handles STM, LTM & User Profile  
│   │── retrieval.py       # FAISS-based vector retrieval  
│   │── database.py        # Empty (Can be used for DB expansion)  
│   │── config.py          # Empty (For future configurations)  
│   └── __init__.py        # Required for module import  
│  
│── tests/  
│   │── test_chatbot.py    # Unit test for chatbot response  
│   │── test_memory.py     # Unit test for memory storage  
│   │── test_retrieval.py  # Unit test for FAISS-based retrieval  
│  
│── frontend/  
│   │── index.html         # Frontend UI for chatbot interaction  
│   │── style.css          # Styling for the chatbot interface  
│   │── script.js          # Handles user interaction  
│  
│── main.py                # Runs chatbot in CLI  
│── .gitignore             # Ignore unnecessary files  
│── readme.md              # Project Documentation  
│── requirements.txt       # Dependencies  
└── faiss_index.bin        # FAISS Vector Store (Auto-Generated)  
```

---

## 🔬 Detailed Explanation of Backend Components  

### **1️⃣ chatbot.py (Main Logic)**  
✅ **Handles user queries** and **manages response generation workflow**.  
✅ **Checks user identity** and **remembers the name**.  
✅ **Queries past memory** or **searches the web** if memory is insufficient.  
✅ **Uses FLAN-T5** to generate responses **based on retrieved information**.  

---

### **2️⃣ memory_manager.py (Memory Handling)**  
✅ **Manages Short-Term Memory (STM)** (last 10 interactions).  
✅ **Stores Long-Term Memory (LTM)** in **ChromaDB**.  
✅ **Handles name retention** when a user introduces themselves.  

---

### **3️⃣ retrieval.py (RAG Retrieval)**  
✅ Uses **FAISS (Facebook AI Similarity Search)** to perform **vector-based similarity searches**.  
✅ Retrieves **contextually relevant responses** from **long-term memory**.  
✅ Ensures **memory relevance before passing it** to the chatbot.  

---

### **4️⃣ DuckDuckGo Web Search**  
✅ When **memory does not contain relevant answers**, the chatbot **searches the web**.  
✅ **Integrates DuckDuckGo API** to **fetch live search results**.  

---

## 🛠 Setup & Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/RAG-Chatbot/RAG-memory-chatbot-backend.git
cd RAG-memory-chatbot-backend
```

### **2️⃣ Create & Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Chatbot**  

✅ **To run in CLI mode**, use:  
```bash
python main.py
```


---

## 📢 Usage  

💬 **Interacting with the Chatbot**  
Once started, you can ask questions like:  

```bash
👤 You: My name is Anarv.
🤖 AI: Got it! I'll remember your name as Anarv.
```

```bash
👤 You: What is my name?
🤖 AI: Your name is Anarv.
```

```bash
👤 You: What is Blockchain?
🤖 AI: (Retrieves from memory OR searches online if needed)
```

```bash
👤 You: clear memory
🤖 AI: 🧹 Memory Cleared: All past interactions erased.
```

---
## 🤔 How it Works?

### **🔹 When a user enters a question:--**

### **1.Check if the user is introducing themselves**
  	•If they say “My name is Anarv”, the chatbot remembers the name.
  	•If they ask “What is my name?”, it retrieves and responds with the name.
### **2.Search Past Memory (Short-Term & Long-Term)**
  	•First, it checks Short-Term Memory (STM) (last 10 interactions).
  	•If no relevant data is found, it searches Long-Term Memory (LTM) using FAISS (a similarity search engine).
  	•If a match is found, it retrieves past responses.
### **3.If Memory Fails, Search the Web**
  	•If no answer is found in memory, it performs a web search using DuckDuckGo.
  	•It then extracts useful information from search results.
### **4.Generating the Response**
  	•Once memory or search data is available, the chatbot creates a prompt for FLAN-T5.
  	•FLAN-T5 then generates a structured and meaningful response.
### **5.Saving the Conversation**
  	•The chatbot stores the user’s query and its response in memory, so it can recall them later.
### **6.Displaying the Response**
  	•The chatbot prints the response in both the terminal and the frontend (web UI).

---
## 🎯 Future Improvements 

🔹 **Multi-User Support**: Extend memory storage for multiple users.  
🔹 **Customizable API Integration**: Allow switching between multiple search engines.  
🔹 **Better RAG Optimization**: Improve **FAISS-based search accuracy**.  
🔹 **GUI Enhancements**: **Advanced chat UI** with **better user experience**.  

---

## 🔥 **Contributing**  

1️⃣ **Fork the repository**  
2️⃣ **Create a feature branch**  
```bash
git checkout -b feature-xyz
```
