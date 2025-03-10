from typing import Any, Dict, List

from app.core.llm import get_llm
from app.core.schema import ChatMessage

# base chat
def chat() -> Dict[str, Any]:
    llm = get_llm()
    response = llm.complete("William Shakespeare is ")
    return response

# async base chat
async def achat() -> Dict[str, Any]:
    llm = get_llm()
    response = await llm.acomplete("William Shakespeare is ")
    return response

# stream chat
async def stream_chat() -> Dict[str, Any]:
    llm = get_llm()
    handle = llm.stream_complete("William Shakespeare is ")
    return handle

# chat with messages
def chat_with_messages(messages: List[ChatMessage]) -> Dict[str, Any]:
    llm = get_llm()
    chat_response = llm.chat(messages)
    return chat_response

# stream chat with messages
def stream_chat_with_messages(messages: List[ChatMessage]) -> Dict[str, Any]:
    llm = get_llm()
    handle = llm.stream_chat(messages)
    return handle

# async stream chat with messages
async def async_stream_chat_with_messages(messages: List[ChatMessage]) -> Dict[str, Any]:
    llm = get_llm()
    response = await llm.astream_chat(messages)
    return response

