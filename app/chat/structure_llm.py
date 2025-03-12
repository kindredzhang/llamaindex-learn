import os
from datetime import datetime
from pydantic import BaseModel, Field
from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate
import json

class DialogueResult(BaseModel):
    """Result of an OpenAI dialogue."""
    sentiment: str = Field(description="The overall sentiment of the response")
    main_topics: list[str] = Field(description="List of main topics discussed")
    word_count: int = Field(description="Number of words in the response")
    timestamp: datetime = Field(description="Time when the response was generated")

llm = OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), api_base=os.getenv("OPENAI_API_BASE"))

# limit struct of llm's answer
# sllm = llm.as_structured_llm(DialogueResult)
# prompt = "Tell me about the importance of renewable energy."
# response = sllm.complete(prompt)

# structured predict
prompt_template = PromptTemplate(
    "Analyze the following text and extract key information.: {text}"
)
response = llm.structured_predict(
    DialogueResult, 
    prompt_template, 
    text="Tell me about the importance of renewable energy."
)
json_output = response.model_dump_json()
print(json.dumps(json.loads(json_output), indent=2))
