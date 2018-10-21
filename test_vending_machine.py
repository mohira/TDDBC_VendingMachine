import unittest
from enum import Enum


class Coin(Enum):
    yen100 = 100


class VendingMachine:
    def __init__(self):
        self.deposit: int = 0

    def insert(self, coin: Coin) -> None:
        self.deposit += coin.value

    def push_コーラボタン(self) -> str:
        return "コーラ"

    def push_烏龍茶ボタン(self) -> str:
        return "烏龍茶"

    def push_炭酸水ボタン(self) -> str:
        return "炭酸水"


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_お題1_コーラボタンを押すとコーラが出る(self):
        self.assertEqual("コーラ", self.vending_machine.push_コーラボタン())

    def test_お題2_100円コインを投入してからコーラボタンを押すとコーラが出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.assertEqual("コーラ", self.vending_machine.push_コーラボタン())

    def test_お題3_100円コインを投入してから烏龍茶ボタンを押すと烏龍茶が出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.assertEqual("烏龍茶", self.vending_machine.push_烏龍茶ボタン())

    def test_お題3_100円コインを投入してから炭酸水ボタンを押すと炭酸水が出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.assertEqual("炭酸水", self.vending_machine.push_炭酸水ボタン())


if __name__ == "__main__":
    unittest.main()
