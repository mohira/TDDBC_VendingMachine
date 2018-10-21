from typing import List

from vending_machine.beverage import Beverage, BeverageCollection
from vending_machine.coin import Coin
from vending_machine.error import DepositShortageError, BeverageNotRegisteredError


class VendingMachine:
    def __init__(self):
        self.take_out_port: List[Beverage] = []
        self.repayment_port = 0
        self.deposit: int = 0

    def insert(self, coin: Coin) -> None:
        self.deposit += coin.value

    def buy(self, beverage_name: str) -> None:
        """
        事前条件:
            - 飲料が存在する
            - 飲料の価格以上の残高である
        事後条件:
            - 取り出し口に購入された飲料が追加される
            - お釣り口にお釣りが返される
            - 残高が0になる
        """
        if not BeverageCollection.exists(beverage_name):
            raise BeverageNotRegisteredError(f"{beverage_name}という飲料はありません")

        beverage = BeverageCollection.__getattr__(beverage_name).value

        if self.deposit < beverage.price:
            raise DepositShortageError("残高が不足しています")

        self.take_out_port.append(beverage)

        self.deposit -= beverage.price
        self.repayment_port += self.deposit
        self.deposit = 0

    def what_can_buy(self) -> List[str]:
        # 購入可能な飲料名の一覧を出す; 名前があればそのまま指定できるからね！
        return [beverage.value.name for beverage in BeverageCollection.line_up() if
                beverage.value.price <= self.deposit]

    def take_out(self) -> List[Beverage]:
        bought_beverages = self.take_out_port

        self.take_out_port = []

        return bought_beverages
