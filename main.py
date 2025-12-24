from agent import initialize_security_agent

def main():
    # Initialize the Multi-Agent System
    manager_agent = initialize_security_agent()

    print("------------------------------------------------")
    print("🛡️  Multi-Agent Security System Online")
    print("   Type 'exit' to stop.")
    print("------------------------------------------------")

    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Manager: Shutting down system. Goodbye!")
            break
        
        if not user_input.strip():
            continue

        try:
            # The Manager receives the input first
            response = manager_agent.run(user_input)
            print(f"Manager: {response}")
        except Exception as e:
            print(f"System Error: {e}")

if __name__ == "__main__":
    main()
