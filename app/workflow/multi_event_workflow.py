import json
from typing import Any, Dict

from llama_index.core.workflow import (Event, StartEvent, StopEvent, Workflow,
                                       step)
from llama_index.llms.openai import OpenAI


class QueryEvent(Event):
    query: str

class AIResponseEvent(Event):
    response: str

class ProcessedEvent(Event):
    processed_data: Dict[str, Any]

class MyWorkflow(Workflow):
    @step
    async def initiate_query(self, ev: StartEvent) -> QueryEvent:
        print(f"Starting workflow with input: {ev.first_input}")
        return QueryEvent(query="Generate a JSON object with information about a random book. ONLY RETURN JSON.")

    @step
    async def get_ai_response(self, ev: QueryEvent) -> AIResponseEvent:
        print(f"Querying AI with: {ev.query}")
        llm = OpenAI("gpt-4o-mini")
        response = await llm.acomplete(ev.query)

        ai_response = response.text
        start = ai_response.find('{')
        end = ai_response.rfind('}')
        if start != -1 and end != -1 and end > start:
            ai_response = ai_response[start:end+1]
        else:
            ai_response = "{}"
        try:
            json_data = json.loads(ai_response)
            cleaned_response = json.dumps(json_data, ensure_ascii=False)
        except json.JSONDecodeError:
            cleaned_response = "{}"
        print(f"Cleaned AI response: {cleaned_response}")
        return AIResponseEvent(response=cleaned_response)

    @step
    async def process_response(self, ev: AIResponseEvent) -> ProcessedEvent:
        print("Processing AI response")
        try:
            processed = json.loads(ev.response)
            return ProcessedEvent(processed_data=processed)
        except json.JSONDecodeError:
            print("Error: AI response is not valid JSON")
            return ProcessedEvent(processed_data={"error": "Invalid JSON"})

    @step
    async def format_output(self, ev: ProcessedEvent) -> StopEvent:
        print("Formatting final output")
        formatted_output = "\n".join([f"{key}: {value}" for key, value in ev.processed_data.items()])
        return StopEvent(result=f"Workflow completed. Book info:\n{formatted_output}")

async def main():
    workflow = MyWorkflow(timeout=30, verbose=True)
    result = await workflow.run(first_input="Start the AI book info workflow.")
    print(f"Final Result:\n{result}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())