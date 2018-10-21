from __future__ import annotations

import unittest

from vending_machine.beverage import BeverageCollection
from vending_machine.coin import Coin
from vending_machine.error import DepositShortageError, BeverageNotRegisteredError
from vending_machine.vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_いくつかの硬貨を使うことができる(self):
        with self.subTest("10円 50円 100円 500円は使える"):
            self.vending_machine.insert(Coin.yen10)
            self.vending_machine.insert(Coin.yen50)
            self.vending_machine.insert(Coin.yen100)
            self.vending_machine.insert(Coin.yen500)

            self.assertEqual(660, self.vending_machine.deposit)

    def test_購入可能な商品名一覧を知ることができる(self):
        with self.subTest("残高0円の場合は何も購入できない"):
            self.assertEqual([], self.vending_machine.what_beverage_names_can_buy())

        with self.subTest("残高100円の場合"):
            self.vending_machine.insert(Coin.yen100)

            expected = [BeverageCollection.コーラ.value.name,
                        BeverageCollection.烏龍茶.value.name,
                        BeverageCollection.炭酸水.value.name]

            self.assertEqual(expected, self.vending_machine.what_beverage_names_can_buy())

        with self.subTest("残高200円の場合"):
            self.vending_machine.insert(Coin.yen100)

            expected = [BeverageCollection.コーラ.value.name,
                        BeverageCollection.烏龍茶.value.name,
                        BeverageCollection.炭酸水.value.name,
                        BeverageCollection.レッドブル.value.name]

            self.assertEqual(expected, self.vending_machine.what_beverage_names_can_buy())

    def test_飲料購入時に残高不足の場合(self):
        with self.subTest("100円以上の残高がないとコーラは購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("コーラ"))

        with self.subTest("100円以上の残高がないと烏龍茶は購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("烏龍茶"))

        with self.subTest("100円以上の残高がないと炭酸水は購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("炭酸水"))

        with self.subTest("200円以上の残高がないとレッドブルは購入できない"):
            self.assertRaises(DepositShortageError, lambda: self.vending_machine.buy("レッドブル"))

    def test_存在しない飲料は購入できない(self):
        self.assertRaises(BeverageNotRegisteredError, lambda: self.vending_machine.buy("HOGE"))

    def test_残高100円で100円の飲料を購入したときの仕様(self):
        self.vending_machine.insert(Coin.yen100)
        self.vending_machine.buy("コーラ")

        with self.subTest("購入した飲料が取り出し口に出てくる"):
            self.assertEqual([BeverageCollection.コーラ.value], self.vending_machine.take_out_port)

        with self.subTest("お釣りは出ない"):
            self.assertEqual(0, self.vending_machine.repayment_port)

        with self.subTest("残高が0円になっている"):
            self.assertEqual(0, self.vending_machine.deposit)

    def test_残高500円で100円の飲料を購入したときの仕様(self):
        self.vending_machine.insert(Coin.yen500)
        self.vending_machine.buy("コーラ")

        with self.subTest("購入した飲料が取り出し口に出てくる"):
            self.assertEqual([BeverageCollection.コーラ.value], self.vending_machine.take_out_port)

        with self.subTest("お釣り400円がお釣り口に出てくる"):
            self.assertEqual(400, self.vending_machine.repayment_port)

        with self.subTest("残高が0円になっている"):
            self.assertEqual(0, self.vending_machine.deposit)


if __name__ == "__main__":
    unittest.main()
