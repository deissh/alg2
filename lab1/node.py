from __future__ import annotations

import uuid
from typing import TypeVar, Generic, List
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    value: T

    id: uuid.UUID = field(default_factory=lambda: uuid.uuid4())
    children: List[Node] = field(default_factory=list)

    def __str__(self):
        return f"Node(value={self.value})"
