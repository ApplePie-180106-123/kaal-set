# 🚀 Kaal Sethu – Time-Travel Generative AI Chatbot  
### A full-stack decade-aware LLM project using Python, FastAPI, React, and Gemini/Gemma models

Kaal Sethu is a Generative AI chatbot capable of simulating conversations from different time periods (1950s → 2010s).  
It adapts its **tone, slang, culture, and technological knowledge** based on the selected decade.

The system also includes **Time-Travel Mode**, where users can switch eras in the middle of the conversation and the bot instantly changes its persona.

---

## ✨ Features

### 🕰️ 1. Decade-Based Persona
Each decade has its own curated JSON dataset containing:
- Slang  
- Cultural references  
- Technology limitations  
- Tone & style rules  
- Example sentences  

Supported decades:
- **1950s**
- **1970s**
- **1990s**
- **2000s**
- **2010s**

---

### 🔄 2. Time-Travel Mode
Users can shift eras dynamically:

Go to 1970s
Shift to 2000s
Take me to 1950s


The chatbot updates:
- tone  
- slang  
- cultural references  
- persona  

---

### 🧠 3. Memory-Driven Dialogue
- Bot remembers last N messages  
- Memory persists across decades  
- Replies feel natural and context-aware  

---

### ⚙️ 4. Modular Backend Architecture (FastAPI)

backend/
│── main.py → FastAPI routes
│── llm_engine.py → Gemini/Gemma inference engine
│── prompt_builder.py → Prompt templates + memory injection
│── decade_loader.py → Loads decade JSON data
│── session_manager.py → Stores mode, decade, history


Supports models:
- **Gemini 2.5 Flash** (fast)
- **Gemma 3** (free + unlimited)

---

### 💬 5. React Frontend
Built with React + Vite:
- Clean chat interface  
- Dropdown decade selector  
- Mode selector (Fixed / Time Travel)  
- Auto-scroll chat view  
- Simple and modern UI  

---

## 🧩 Architecture Overview

Frontend (React)
|
| POST: /chat
v
Backend (FastAPI)
├── decade_loader.py
├── prompt_builder.py
├── llm_engine.py
├── session_manager.py
└── main.py
|
v
LLM (Gemini / Gemma)

kaal-sethu/
│
├── backend/
│ ├── main.py
│ ├── llm_engine.py
│ ├── prompt_builder.py
│ ├── decade_loader.py
│ ├── session_manager.py
│
├── data/
│ ├── 1950s.json
│ ├── 1970s.json
│ ├── 1990s.json
│ ├── 2000s.json
│ ├── 2010s.json
│
├── frontend/
│ ├── src/
│ ├── package.json
│
├── .gitignore
├── README.md
└── venv/


---

## 🛠️ Tech Stack

### **Frontend**
- React  
- Vite  
- Axios  

### **Backend**
- Python  
- FastAPI  
- Uvicorn  
- google-generativeai  
- Gemma 3 models  
- dotenv  

### **Data**
- Custom-curated JSON datasets  

---

## 🚀 Running the Project

### 1️⃣ Start Backend

```bash
cd kaal-sethu
source venv/bin/activate
uvicorn backend.main:app --reload


Open API Docs:
👉 http://127.0.0.1:8000/docs

2️⃣ Start Frontend
cd frontend
npm install
npm run dev


Visit:
👉 http://localhost:5173/

🧪 Example Chat Commands
Hello!
Go to 1970s
Talk like the 1950s
Shift to 2010s
Repeat what I said earlier.

🔮 Future Enhancements

Voice-based time travel

Animated decade transitions

Persistent conversation history

Authentication + user preferences

Deployment to Vercel + Render

Customizable chatbot personalities