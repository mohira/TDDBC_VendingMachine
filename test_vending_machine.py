import unittest
from dataclasses import dataclass
from enum import Enum


class Coin(Enum):
    yen100 = 100


@dataclass(frozen=True)
class Beverage:
    name: str
    price: int


class BeverageCollection(Enum):
    コーラ = Beverage(name="コーラ", price=100)
    炭酸水 = Beverage(name="炭酸水", price=100)
    烏龍茶 = Beverage(name="烏龍茶", price=100)
    レッドブル = Beverage(name="レッドブル", price=200)


class 残高不足Error(Exception):
    pass


class VendingMachine:
    def __init__(self):
        self.deposit: int = 0

    def insert(self, coin: Coin) -> None:
        self.deposit += coin.value

    def push_コーラボタン(self) -> Beverage:
        コーラ = BeverageCollection.コーラ
        if self.deposit < コーラ.value.price:
            raise 残高不足Error("コーラは買えないよ")

        return コーラ

    def push_烏龍茶ボタン(self) -> Beverage:
        烏龍茶 = BeverageCollection.烏龍茶
        if self.deposit < 烏龍茶.value.price:
            raise 残高不足Error("烏龍茶は買えないよ")

        return 烏龍茶

    def push_炭酸水ボタン(self) -> Beverage:
        炭酸水 = BeverageCollection.炭酸水
        if self.deposit < 炭酸水.value.price:
            raise 残高不足Error("烏龍茶は買えないよ")

        return 炭酸水

    def push_レッドブルボタン(self) -> Beverage:
        レッドブル = BeverageCollection.レッドブル

        if self.deposit < レッドブル.value.price:
            raise 残高不足Error("レッドブルは買えないよ")

        return レッドブル


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_お題2_100円コインを投入してからコーラボタンを押すとコーラが出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.assertEqual(BeverageCollection.コーラ, self.vending_machine.push_コーラボタン())

    def test_お題3_100円コインを投入してから烏龍茶ボタンを押すと烏龍茶が出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.assertEqual(BeverageCollection.烏龍茶, self.vending_machine.push_烏龍茶ボタン())

    def test_お題3_100円コインを投入してから炭酸水ボタンを押すと炭酸水が出る(self):
        self.vending_machine.insert(Coin.yen100)

        self.assertEqual(BeverageCollection.炭酸水, self.vending_machine.push_炭酸水ボタン())

    def test_お題4_200円の残高があるときにレッドブルボタンを押すとレッドブルが出る(self):
        self.vending_machine.insert(Coin.yen100)
        self.vending_machine.insert(Coin.yen100)

        self.assertEqual(BeverageCollection.レッドブル, self.vending_machine.push_レッドブルボタン())

    def test_残高不足の場合の対応(self):
        with self.subTest("200円以上の残高がないとレッドブルボタンを押してもレッドブルは出ない"):
            self.assertRaises(残高不足Error, lambda: self.vending_machine.push_レッドブルボタン())

        with self.subTest("100円以上の残高がないとコーラボタンを押してもコーラは出ない"):
            self.assertRaises(残高不足Error, lambda: self.vending_machine.push_コーラボタン())

        with self.subTest("200円以上の残高がないと烏龍茶ボタンを押しても烏龍茶は出ない"):
            self.assertRaises(残高不足Error, lambda: self.vending_machine.push_烏龍茶ボタン())

        with self.subTest("200円以上の残高がないと炭酸水ボタンを押しても炭酸水は出ない"):
            self.assertRaises(残高不足Error, lambda: self.vending_machine.push_炭酸水ボタン())


if __name__ == "__main__":
    unittest.main()
