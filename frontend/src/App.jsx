import { useState } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [decade, setDecade] = useState("1990s");
  const [mode, setMode] = useState("fixed"); // fixed or time-travel
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "User", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: input,
        decade: decade,
        mode: mode,
      });

      const botMsg = {
        role: "Bot",
        text: res.data.reply,
        decade: res.data.current_decade,
      };

      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "Bot", text: "[Error connecting to backend]" },
      ]);
    }

    setInput("");
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Kaal Sethu Chatbot</h1>

      <div style={styles.controls}>
        <select value={decade} onChange={(e) => setDecade(e.target.value)} style={styles.dropdown}>
          <option value="1950s">1950s</option>
          <option value="1970s">1970s</option>
          <option value="1990s">1990s</option>
          <option value="2000s">2000s</option>
          <option value="2010s">2010s</option>
        </select>

        <select value={mode} onChange={(e) => setMode(e.target.value)} style={styles.dropdown}>
          <option value="fixed">Fixed Mode</option>
          <option value="time-travel">Time Travel Mode</option>
        </select>
      </div>

      <div style={styles.chatBox}>
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              ...styles.message,
              alignSelf: msg.role === "User" ? "flex-end" : "flex-start",
              background: msg.role === "User" ? "#cce5ff" : "#e8e8e8",
              color: "#000000" // ← ADD THIS
            }}
          >
            <strong>{msg.role}:</strong> {msg.text}
            {msg.role === "Bot" && (
              <div style={styles.decadeTag}>📅 {msg.decade}</div>
            )}
          </div>
        ))}

        {loading && <div style={styles.loading}>⏳ Thinking...</div>}
      </div>

      <div style={styles.inputArea}>
        <input
          style={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type message..."
        />
        <button style={styles.button} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: { width: "60%", margin: "auto", marginTop: 40, fontFamily: "Arial" },
  title: { textAlign: "center" },
  controls: { display: "flex", gap: 10, marginBottom: 10 },
  dropdown: { padding: 8, fontSize: 16 },
  chatBox: {
    height: "60vh",
    overflowY: "auto",
    border: "1px solid #ccc",
    borderRadius: 8,
    padding: 10,
    display: "flex",
    flexDirection: "column",
  },
  message: {
    padding: 10,
    margin: 5,
    borderRadius: 6,
    maxWidth: "70%",
    position: "relative",
  },
  decadeTag: { fontSize: 12, opacity: 0.7, marginTop: 4 },
  loading: { textAlign: "center", padding: 10, fontStyle: "italic" },
  inputArea: { display: "flex", marginTop: 10 },
  input: { flex: 1, padding: 10, fontSize: 16 },
  button: { padding: "10px 20px", fontSize: 16 },
};

export default App;
