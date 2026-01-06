#🛡️ Multi-Agent Security Operations Center (SOC)
A hierarchical AI system powered by LangChain and Google Gemini, designed to simulate a Security Operations Center. This project demonstrates a "Manager-Worker" agent architecture where a Manager Agent orchestrates user interactions and delegates technical tasks to a specialized Security Analyst Agent.

##🚀 Key Features
1. Multi-Agent Collaboration: Implements a hierarchical structure where a conversational Manager delegates specific tasks to a technical Analyst.
2. Hierarchical Memory: Agents share context using ConversationBufferMemory.
3. Dual Interfaces:
• CLI Mode: Interact directly via the terminal.
• Web Dashboard: A full-stack implementation using Flask (Backend API) and Streamlit (Frontend UI).
4. Custom Security Tools:
🔐 Password Strength Checker: Validates length and complexity.
#️⃣ Integrity Hasher: Generates SHA-256 hashes for data integrity verification.
👋 Greeter: Context-aware interaction.

##🛠️ Tech Stack
Python 3.10+
LangChain: For agent orchestration and tool management.
Google Gemini (via langchain-google-genai): The LLM brain (gemini-2.5-flash).
Flask: REST API backend.
Streamlit: Interactive frontend dashboard.

##📂 Project Structure
Plaintext

├── agent.py       # Core logic: Initializes Manager and Analyst agents
├── tools.py       # Custom tools (Password check, Hashing, Greeting)
├── prompts.py     # System instructions (Prompts) for Manager and Analyst
├── memory.py      # Shared memory configuration
├── main.py        # Entry point for CLI (Command Line Interface)
├── api.py         # Flask Entry point (Backend API) - (referenced as MAIN2.PY)
├── frontend.py    # Streamlit Entry point (Web Dashboard)
└── .env           # Environment variables (API Keys)

##🧠 Agent Architecture
This system uses a Conversational ReAct pattern for the Manager and a Zero-Shot ReAct pattern for the Analyst.

1. The User sends a query (e.g., "Check if 'Admin123' is a strong password").
2. The Manager receives the query. It realizes this is a technical task based on its system prompt (prompts.py).
3. The Delegation: The Manager calls the AskSecurityAnalyst tool.
4. The Analyst receives the sub-task, executes the PasswordStrengthChecker tool defined in tools.py, and returns the raw data.
5. The Result: The Manager interprets the Analyst's output and summarizes it for the User.

##📝 Example Queries
Try these in the dashboard:
"Hello, my name is Alice." (Tests Memory/Greeting)
"Check the password strength of 'P@ssw0rd123!'." (Tests Analyst Delegation)
"Generate a SHA-256 hash for the file 'malware.exe'." (Tests Hashing Tool)

##🌐 Working Protoype Link
(https://securityoperationscenter.streamlit.app/)
