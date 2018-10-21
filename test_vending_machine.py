from __future__ import annotations

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
    烏龍茶 = Beverage(name="烏龍茶", price=100)
    炭酸水 = Beverage(name="炭酸水", price=100)
    レッドブル = Beverage(name="レッドブル", price=200)

    @classmethod
    def line_up(cls):
        return [cls.コーラ, cls.烏龍茶, cls.炭酸水, cls.レッドブル]

    @classmethod
    def name_list(cls):
        return [beverage.name for beverage in cls.line_up()]

    @classmethod
    def exists(cls, name: str) -> bool:
        return name in cls.name_list()


class DepositShortageError(Exception):
    pass


class BeverageNotRegisteredError(Exception):
    pass


class VendingMachine:
    def __init__(self):
        self.deposit: int = 0

    def insert(self, coin: Coin) -> None:
        self.deposit += coin.value

    def buy(self, beverage_name: str) -> Beverage:
        if not BeverageCollection.exists(beverage_name):
            raise BeverageNotRegisteredError(f"{beverage_name}という飲料はありません")

        beverage = BeverageCollection.__getattr__(beverage_name)

        if self.deposit < beverage.value.price:
            raise DepositShortageError("残高が不足しています")

        # 購入できたら残高を差し引かないと何度でも購入できてしまう
        self.deposit -= beverage.value.price

        return beverage


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_必要な残高があれば飲料を購入できる(self):
        with self.subTest("100円あればコーラを購入できる"):
            self.vending_machine.insert(Coin.yen100)
            self.assertEqual(BeverageCollection.コーラ, self.vending_machine.buy("コーラ"))

        with self.subTest("100円あれば烏龍茶を購入できる"):
            self.vending_machine.insert(Coin.yen100)
            self.assertEqual(BeverageCollection.烏龍茶, self.vending_machine.buy("烏龍茶"))

        with self.subTest("100円あれば炭酸水を購入できる"):
            self.vending_machine.insert(Coin.yen100)
            self.assertEqual(BeverageCollection.炭酸水, self.vending_machine.buy("炭酸水"))

        with self.subTest("200円あればレッドブルを購入できる"):
            self.vending_machine.insert(Coin.yen100)
            self.vending_machine.insert(Coin.yen100)

            self.assertEqual(BeverageCollection.レッドブル, self.vending_machine.buy("レッドブル"))

    def test_残高不足の場合の対応(self):
        with self.subTest("100円以上の残高がないとコーラは購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("コーラ"))

        with self.subTest("100円以上の残高がないと烏龍茶は購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("烏龍茶"))

        with self.subTest("100円以上の残高がないと炭酸水は購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("炭酸水"))

        with self.subTest("200円以上の残高がないとレッドブルは購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("レッドブル"))

    def test_飲料を購入したら価格の分だけ残高を減らす(self):
        self.vending_machine.insert(Coin.yen100)
        self.vending_machine.buy("コーラ")

        self.assertEqual(0, self.vending_machine.deposit)

    def test_存在しない飲料は購入できない(self):
        self.assertRaises(BeverageNotRegisteredError, lambda: self.vending_machine.buy("HOGE"))


if __name__ == "__main__":
    unittest.main()
