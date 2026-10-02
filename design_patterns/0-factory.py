#!/usr/bin/env python3
"""
0-factory.py: Extending a vehicle factory registry.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def mode(self) -> str:
        pass


class Bus(Vehicle):
    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {}

    def register_kind(self, kind: str, cls: type) -> None:
        self._registry[kind] = cls

    def create(self, kind: str) -> Vehicle:
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main():
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    
    # Registering the new scooter type
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
