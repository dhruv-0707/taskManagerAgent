from dotenv import load_dotenv
from src.agent.core import create_agent_graph

# Load environment variables (API Key)
load_dotenv()

def main():
    print("Initializing Agent...")
    try:
        agent = create_agent_graph()
    except Exception as e:
        print(f"Failed to initialize agent. Check your .env file and API keys.\nError: {e}")
        return

    # In LangGraph, we use thread_id for session management
    thread_id = "user_session_1"
    config = {"configurable": {"thread_id": thread_id}}
    
    print(f"Task Manager Agent Ready! (Session ID: {thread_id})")
    print("Type 'exit' to quit.\n")
    print("Example commands: 'Add a task to buy milk', 'List my tasks', 'Mark task 1 as completed'")

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            # 5. Validation & Usage: The agent is invoked with the new LangGraph format
            # Input is a list of messages (or just the latest user message)
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            
            # Extract the last message content which is the assistant's response
            if response and "messages" in response and len(response["messages"]) > 0:
                print(f"Agent: {response['messages'][-1].content}\n")
            else:
                print("Agent: (No response)\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
