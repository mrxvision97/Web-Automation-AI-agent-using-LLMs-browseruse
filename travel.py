import asyncio
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from browser_use import Agent

async def run_search():
    # Initialize the Qwen2.5 language model
    llm = ChatOllama(
        model='qwen2.5:7b',  # Using the 7B parameter version of Qwen2.5
        num_ctx=128000,      # Context window size
    )

    # Prompt the user to enter a task description
    task_description = input("Enter the task description: ")

    # Define a prompt to instruct the LLM to break down the task
    prompt = (
        "Please break down the following task into a list of actionable steps "
        "that a web automation agent can execute. Each step should be a simple, "
        "specific instruction, such as 'go to [website]', 'enter [text] into [field]', "
        "'click [button]', etc. List each step on a new line.\n"
        f"Task: {task_description}"
    )

    # Generate the list of steps using the language model
    response = llm([HumanMessage(content=prompt)])

    # Parse the response into a clean list of steps
    steps = [step.strip() for step in response.content.split('\n') if step.strip()]

    # Initialize the Agent with the generated steps and the language model
    agent = Agent(
        task=tuple(steps),       # Convert steps to a tuple, as expected by Agent
        llm=llm,                 # Pass the same LLM instance for execution
        max_actions_per_step=1,  # Limit to one action per step
    )

    # Execute the steps using the agent
    await agent.run()

if __name__ == '__main__':
    # Run the async function
    asyncio.run(run_search())