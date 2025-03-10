from dotenv import load_dotenv

load_dotenv()

from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow

# Agent is a special type of workflow that uses a function calling LLM.
# So can define your function calling LLM to reference out data sources, etc.

def multiply(a: float, b: float) -> float:
    return a * b

def add(a: float, b: float) -> float:
    return a + b

llm = OpenAI("gpt-4o")

workflow = AgentWorkflow.from_tools_or_functions(
    [multiply, add],
    llm=llm,
    system_prompt="You are an agent that can perform basic mathematical operations using tools.",
)

async def main():
    response = await workflow.run(user_msg="What is 20+(2*4)?")
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())