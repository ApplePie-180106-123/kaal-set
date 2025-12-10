class SessionState:
    def __init__(self):
        self.current_decade = "1990s"
        self.mode = "fixed"
        self.history = []  # conversation memory

    def set_decade(self, decade):
        self.current_decade = decade

    def get_decade(self):
        return self.current_decade

    def add_message(self, role, message):
        self.history.append({"role": role, "message": message})

        # Limit memory to last 8 messages
        if len(self.history) > 8:
            self.history.pop(0)

    def get_memory(self):
        return "\n".join([f"{m['role']}: {m['message']}" for m in self.history])


# Create a single global session
session = SessionState()
