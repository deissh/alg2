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

    def test_insert_as_arr(self):
        ht = HashTable[int](cap=5)

        ht.add(1)
        ht.add(2)
        ht.add(3)

        print('miss=', ht.hash_miss)
