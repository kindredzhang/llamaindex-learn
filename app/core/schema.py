# enum system, user, assistant

from enum import Enum

from llama_index.core.llms import ChatMessage


class MessageRole(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

    def __str__(self):
        return self.value

class ChatMessage(ChatMessage):
    def __init__(self, role: MessageRole, content: str):
        super().__init__(role=role.value, content=content)