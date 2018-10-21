import unittest
from enum import Enum


class Coin(Enum):
    yen100 = 100


class VendingMachine:
    def __init__(self):
        self.deposit = 0

    def push_コーラボタン(self) -> str:
        return "コーラ"

    def insert(self, coin: Coin) -> None:
        self.deposit += coin.value


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_お題1_コーラボタンを押すとコーラが出る(self):
        self.assertEqual("コーラ", self.vending_machine.push_コーラボタン())

    def test_お題2_100円コインを投入してからコーラボタンを押すとコーラが出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.assertEqual("コーラ", self.vending_machine.push_コーラボタン())


if __name__ == "__main__":
    unittest.main()
