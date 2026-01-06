# 🛡️ Multi-Agent Security Operations Center (SOC)

A hierarchical AI system built with **LangChain** and **Google Gemini** that simulates a **Security Operations Center (SOC)**. This project demonstrates a **Manager–Worker (Manager–Analyst)** agent architecture, where a conversational Manager Agent orchestrates user interactions and delegates technical tasks to a specialized Security Analyst Agent.

---

## 🚀 Key Features

* **Multi-Agent Collaboration**
  Hierarchical design where a Manager agent handles conversation flow and delegates technical tasks to an Analyst agent.

* **Hierarchical Memory**
  Shared context between agents using `ConversationBufferMemory` for coherent, stateful interactions.

* **Dual Interfaces**

  * **CLI Mode**: Interact directly via the terminal.
  * **Web Dashboard**: Full-stack setup with Flask (backend API) and Streamlit (frontend UI).

* **Custom Security Tools**

  * 🔐 **Password Strength Checker**: Validates password length and complexity.
  * #️⃣ **Integrity Hasher**: Generates SHA-256 hashes for data integrity verification.
  * 👋 **Greeter**: Context-aware greeting and memory-based interaction.

---

## 🛠️ Tech Stack

* **Python** 3.10+
* **LangChain** – Agent orchestration and tool management
* **Google Gemini** (`langchain-google-genai`) – LLM engine (`gemini-2.5-flash`)
* **Flask** – REST API backend
* **Streamlit** – Interactive web dashboard (frontend)

---

## 📂 Project Structure

```plaintext
├── agent.py        # Core logic: initializes Manager and Analyst agents
├── tools.py        # Custom tools (password check, hashing, greeting)
├── prompts.py      # System prompts for Manager and Analyst agents
├── memory.py       # Shared memory configuration
├── main.py         # CLI entry point
├── api.py          # Flask backend entry point (referenced as MAIN2.PY)
├── frontend.py     # Streamlit web dashboard entry point
└── .env            # Environment variables (API keys)
```

---

## 🧠 Agent Architecture

This system follows a **Conversational ReAct** pattern for the Manager agent and a **Zero-Shot ReAct** pattern for the Analyst agent.

### Workflow

1. **User Query**
   Example: `"Check if 'Admin123' is a strong password"`

2. **Manager Agent**
   Receives the query and determines whether it is conversational or technical based on its system prompt.

3. **Task Delegation**
   If technical, the Manager invokes the `AskSecurityAnalyst` tool.

4. **Analyst Agent**
   Executes the appropriate security tool (e.g., password strength checker, hashing tool) and returns raw results.

5. **Final Response**
   The Manager interprets the Analyst’s output and presents a clear, user-friendly summary.

---

## 📝 Example Queries

Try the following in the CLI or Web Dashboard:

* `Hello, my name is Alice.`
  *Tests greeting and shared memory.*

* `Check the password strength of 'P@ssw0rd123!'.`
  *Tests Manager → Analyst delegation and password checker.*

* `Generate a SHA-256 hash for the file 'malware.exe'.`
  *Tests integrity hashing tool.*

---

## 🌐 Live Prototype

🔗 **Streamlit App**: [https://securityoperationscenter.streamlit.app/](https://securityoperationscenter.streamlit.app/)

---
