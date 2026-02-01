import chainlit as cl
from dotenv import load_dotenv
from src.agent.core import create_agent_graph
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("agent", create_agent_graph())
    # We can use the chainlit session id as the thread_id for persistence
    cl.user_session.set("config", {"configurable": {"thread_id": cl.user_session.get("id")}})
    
    await cl.Message(content="Hello! I am your Task Management Agent. How can I help you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    config = cl.user_session.get("config")
    
    # Create a HumanMessage from the user's input
    input_message = HumanMessage(content=message.content)
    
    msg = cl.Message(content="")
    await msg.send()
    
    # Run the agent using ainvoke to get the final response
    response = await agent.ainvoke(
        {"messages": [input_message]}, 
        config=config
    )
    
    # The state 'messages' contains the full history. We want the last message from the AI.
    if response and "messages" in response and len(response["messages"]) > 0:
        last_message = response["messages"][-1]
        msg.content = last_message.content
    else:
        msg.content = "No response from agent."
    
    await msg.update()
