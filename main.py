import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory

load_dotenv()

#WEEK 1
def greet(name: str):
    return f"Hello {name}, I am your Security Advisor Agent!"

greet_tool = Tool(
    name="GreetingTool",
    func=greet,
    description="Use this to greet a person by name. Input should be the name."
)

tools = [greet_tool]

#WEEK 2
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.7 
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=True
)

def main():
    print("------------------------------------------------")
    print("🤖 Security Agent is Ready!")
    print("   Capabilities: Greeting, Device Security Advice")
    print("   Type 'exit', 'quit', or 'q' to stop.")
    print("------------------------------------------------")

    while True:
            # Get user input
            user_input = input("\nYou: ")
            
            # Check for exit condition
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Agent: Stay secure! Goodbye.")
                break
            
            if not user_input.strip():
                continue

            # Run the agent
            response = agent.run(user_input)
            
            # Print response
            print(f"Agent: {response}")

if __name__ == "__main__":
    main()