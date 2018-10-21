from vending_machine.beverage import Beverage, BeverageCollection
from vending_machine.coin import Coin
from vending_machine.error import DepositShortageError, BeverageNotRegisteredError


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
