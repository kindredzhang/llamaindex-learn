from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI

def generate_song(name: str, artist: str) -> str: 
    return f"{name} by {artist} is a great song. this song's genre is {artist}'s genre."

tool = FunctionTool.from_defaults(
    fn=generate_song,
)

# gpt-4o support function calling
llm = OpenAI("gpt-4o")
response = llm.predict_and_call(
    [tool],
    "random generate 'name' and 'artist' and call the 'generate_song' function."
)

print(response)

