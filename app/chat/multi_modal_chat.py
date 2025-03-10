from llama_index.core.llms import ChatMessage, ImageBlock, TextBlock
from llama_index.llms.openai import OpenAI


def multi_modal_chat():
    llm = OpenAI(
        model="gpt-4o-mini",
    )

    image_url = "https://avatars.githubusercontent.com/u/120791467?v=4"
    messages = [
        ChatMessage(
            role="system",
            content="You are a helpful assistant. please use 10 words or less. and use chinese answer.",
        ),
        ChatMessage(
            role="user",
            blocks=[
                ImageBlock(url=image_url),
                TextBlock(text="Describe the image in a few sentences."),
            ],
        )
    ]
    chat_response = llm.chat(messages)
    return chat_response

if __name__ == "__main__":
    response = multi_modal_chat()
    print(response)