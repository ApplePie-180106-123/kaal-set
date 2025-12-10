The bot instantly changes its persona + dialogue rules.

---

### 🧠 **3. Conversation Memory**
- Bot remembers past 8 messages  
- Responses remain context-aware  
- Works across decade transitions  

---

### ⚙️ **4. Modular Backend Architecture**
Backend built with **FastAPI**, containing:
- `llm_engine.py` → Gemini/Gemma LLM handler  
- `prompt_builder.py` → Prompt templates + memory injection  
- `decade_loader.py` → Loads curated JSON per decade  
- `session_manager.py` → Tracks mode, decade, and conversation history  
- `main.py` → API layer  

This ensures clean maintainability & future scalability.

---

### 💬 **5. React Frontend**
- Live chat interface  
- Decade dropdown  
- Mode selector (Fixed / Time-Travel)  
- Auto-scroll chat  
- Clean message bubbles  
- API integration with Axios  

---

## 🧩 Architecture Overview

