from dataclasses import dataclass
from enum import Enum
from json import dumps, loads


class MessageType(str, Enum):
    error = 'error'
    message = 'message'


@dataclass
class Message:
    content: str
    type: MessageType

    def to_json(self) -> str:
        return dumps({'content': self.content, 'type': self.type})

    @classmethod
    def from_json(cls, json: str) -> 'Message':
        _dict = loads(json)
        return cls(content=_dict['content'], type=MessageType(_dict['type']))
