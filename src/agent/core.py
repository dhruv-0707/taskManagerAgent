from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from src.tools.task_tools import add_task, list_tasks, update_task, delete_task



def create_agent_graph():
    # Initialize LLM
    # Switched back to 'gemini-flash-latest' per user request
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0, 
        max_retries=5, # Increased retries to handle rate limits better
    )

    # Validate Tools
    tools = [add_task, list_tasks, update_task, delete_task]

    # Define System Prompt
    system_prompt = (
        "You are an intelligent Task Management Agent.\n"
        "Your goal is to help the user manage their todo list efficiently.\n"
        "You can add, list, update (mark completed, change priority), and delete tasks.\n"
        "Always confirm the action you took. If asked to list tasks, format them nicely."
    )

    # 4. Memory: Initialize memory saver for persistence
    memory = MemorySaver()

    # Create the Agent (The Brain & Body)
    agent_graph = create_react_agent(
        llm, 
        tools, 
        prompt=system_prompt,
        checkpointer=memory,
    )

    return agent_graph
