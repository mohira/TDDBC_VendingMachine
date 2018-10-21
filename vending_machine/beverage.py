from dataclasses import dataclass
from enum import Enum


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
