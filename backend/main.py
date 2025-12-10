from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from backend.decade_loader import load_decade_data
from backend.prompt_builder import build_decade_prompt, build_time_travel_prompt
from backend.llm_engine import generate_response
from backend.session_manager import session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    mode: str  # "fixed" or "time-travel"
    decade: str = None


@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message
    mode = req.mode

    # save user message
    session.add_message("User", user_message)

    # FIXED MODE
    if mode == "fixed":
        decade = req.decade or "1990s"
        session.set_decade(decade)

        decade_data = load_decade_data(decade)
        memory = session.get_memory()
        prompt = build_decade_prompt(decade_data, user_message, memory)

    # TIME TRAVEL MODE
    else:
        memory = session.get_memory()

        # detect commands like "go to 1970s"
        lower_msg = user_message.lower()
        for d in ["1950s", "1970s", "1990s", "2000s", "2010s"]:
            if d in lower_msg:
                session.set_decade(d)

        prompt = build_time_travel_prompt(session.get_decade(), user_message, memory)

    reply = generate_response(prompt)
    session.add_message("Assistant", reply)

    return {
        "reply": reply,
        "current_decade": session.get_decade(),
        "mode": mode
    }
