from rentomatic.domain.room import Room
from typing import List, Dict, Any


class MemRepo:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data: List[Dict[str, Any]] = data

    def list(self) -> List[Room]:
        return [Room.from_dict(i) for i in self.data]
