import asyncio
from re import A

from app.chat import chat
from app.schema import MessageRole, ChatMessage

async def main():

    # base chat
    # response = app.chat.chat()

    # async base chat
    # response = await app.chat.achat()

    # stream chat
    # handle = await app.chat.stream_chat()
    # for token in handle:
    #     print(token.delta, end="", flush=True)

    # chat with messages
    # chat_messages = [
    #     ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant. please use 10 words or less. and use chinese answer."),
    #     ChatMessage(role=MessageRole.USER, content="William Shakespeare is ")
    # ]
    # response = app.chat.chat_with_messages(chat_messages)

    # stream chat with messages
    # chat_messages = [
    #     ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant. please use 10 words or less. and use chinese answer."),
    #     ChatMessage(role=MessageRole.USER, content="William Shakespeare is ")
    # ]
    # response = app.chat.stream_chat_with_messages(chat_messages)

    # async stream chat with messages
    # chat_messages = [
    #     ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant. please use 10 words or less. and use chinese answer."),
    #     ChatMessage(role=MessageRole.USER, content="William Shakespeare is ")
    # ]
    # response = await app.chat.async_stream_chat_with_messages(chat_messages)
    # async for token in response:
    #     print(token.delta, end="", flush=True)

    # output response
    print(response)

if __name__ == "__main__":
    asyncio.run(main())