#!/usr/bin/env python3
"""
2-decorator.py: Implementing CaramelDecorator using
the Decorator design pattern.
"""
from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class Coffee(Beverage):
    def cost(self) -> float:
        return 50.0

    def description(self) -> str:
        return "Coffee"


class BeverageDecorator(Beverage, ABC):
    def __init__(self, inner: Beverage):
        self._inner = inner


class MilkDecorator(BeverageDecorator):
    def cost(self) -> float:
        return self._inner.cost() + 10.0

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    def cost(self) -> float:
        return self._inner.cost() + 5.0

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    def cost(self) -> float:
        return self._inner.cost() + 15.0

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main():
    beverage1 = MilkDecorator(Coffee())
    print(f"{beverage1.description()} {int(beverage1.cost())}")

    beverage2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{beverage2.description()} {int(beverage2.cost())}")

    beverage3 = CaramelDecorator(
        MilkDecorator(SugarDecorator(Coffee()))
    )
    print(f"{beverage3.description()} {int(beverage3.cost())}")


if __name__ == "__main__":
    main()
