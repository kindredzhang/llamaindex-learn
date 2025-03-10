from llama_index.llms.openai import OpenAI
import os

def get_llm(model="gpt-4o-mini"):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

    llm = OpenAI(
        model=model,
        temperature=0.7,
        max_tokens=1000,
        api_key=OPENAI_API_KEY,
        api_base=OPENAI_API_BASE,
    )
    return llm