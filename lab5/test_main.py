from unittest import TestCase
from .main import PearsonHasher, HashTable


class TestPearsonHasher(TestCase):
    def test_hash(self):
        h = PearsonHasher()
        assert h.hash("some text") == h.hash("some text")


class TestHashTable(TestCase):
    def test_table(self):
        ht = HashTable[int](cap=5)

        for i in range(10):
            ht.add(i)

        print('miss=', ht.hash_miss)
