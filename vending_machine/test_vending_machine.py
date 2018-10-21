from __future__ import annotations

import unittest

from vending_machine.beverage import BeverageCollection
from vending_machine.coin import Coin
from vending_machine.error import DepositShortageError, BeverageNotRegisteredError
from vending_machine.vending_machine import VendingMachine


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
