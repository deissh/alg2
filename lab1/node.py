from __future__ import annotations

import uuid
from typing import TypeVar, Generic, List, Optional
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    value: T

    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    children: List[Optional[Node]] = field(default_factory=list)

    def __str__(self):
        return f"Node(id={self.id}, value={self.value})"
