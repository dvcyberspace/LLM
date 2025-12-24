import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType, Tool

from tools import security_tools
from memory import get_memory
# IMPORT THE PROMPTS HERE
from prompts import MANAGER_PROMPT, ANALYST_PROMPT

load_dotenv()

def initialize_security_agent():
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0
    )

    # --- 1. THE ANALYST (Worker) ---
    analyst_agent = initialize_agent(
        tools=security_tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        # INJECT ANALYST PROMPT HERE
        agent_kwargs={'prefix': ANALYST_PROMPT} 
    )

    def ask_analyst(query: str):
        return analyst_agent.run(query)

    analyst_tool = Tool(
        name="AskSecurityAnalyst",
        func=ask_analyst,
        description="Delegate technical tasks (password/hash) to the Analyst."
    )

    # --- 2. THE MANAGER (Orchestrator) ---
    shared_memory = get_memory()
    manager_tools = [analyst_tool]

    manager_agent = initialize_agent(
        tools=manager_tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=shared_memory,
        verbose=True,
        handle_parsing_errors=True,
        # INJECT MANAGER PROMPT HERE
        agent_kwargs={'prefix': MANAGER_PROMPT}
    )
    
    return manager_agent