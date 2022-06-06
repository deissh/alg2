from typing import Any, List, TypeVar, Generic

import abc
import random

T = TypeVar("T")


class Hasher(abc.ABC):
    @abc.abstractmethod
    def hash(self, data: Any):
        pass


class PearsonHasher(Hasher):
    _table: bytes

    def __init__(self, table_size: int = 1024):
        self._table = random.randbytes(table_size)

    def hash(self, data: Any) -> int:
        h = 0
        ba = bytes(data, 'utf-8') if type(data) == str else bytes(data)

        for byte in ba:
            idx = h ^ byte
            h = self._table[idx % len(self._table)]

        return h


class HashTable(Generic[T]):
    _storage: List[T]
    _hasher: Hasher

    hash_miss: int

    def __init__(self, cap: int = 100):
        self._storage = cap * [None]
        self._hasher = PearsonHasher()
        self.hash_miss = 0

    def __len__(self):
        return len(self._storage)

    def _add(self, value: T, index: int = 0):
        index = (self._hasher.hash(value) + index) % len(self._storage)
        if self._storage[index] is not None:
            if self._storage[index] == value:
                return
            if index > len(self._storage):
                return

            index += 1
            self.hash_miss += 1
            return self._add(value, index)
        self._storage[index] = value

    def add(self, value: T):
        try:
            return self._add(value)
        except Exception:
            pass
