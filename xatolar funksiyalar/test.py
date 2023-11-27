import unittest

from xatolar import *


class TestSonlar(unittest.TestCase):
    def katta_son(self):
        sonlar = my_max(11, 32, 12)
        self.assertEqual(sonlar, 32)


class TestKatta(unittest.TestCase):
    def katta_harf(self):
        matnlar = kata_harf(["apple", "banana", "cherry"])
        self.assertEqual(matnlar, "Apple Banan Cherry")


unittest.main()
