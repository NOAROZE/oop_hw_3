from abc import ABC, abstractmethod
from typing_extensions import override
from interfaces import Chargeable, Drivable


class Vehicle(ABC):
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"model: {self.model}"

    @abstractmethod
    def move(self):
        pass


class ElectricCar(Vehicle, Chargeable, Drivable):
    def __init__(self, model, battery_level):
        super().__init__(model)
        self.battery_level = battery_level

    def __str__(self):
        return f"{super().__str__()}, battery level: {self.battery_level}"

    @override
    def move(self):
        return f"{super().__str__()} is move silently"

    @override
    def charge(self):
        return f"{super().__str__()} is charging"

    @override
    def drive(self):
        return f"{super().__str__()} is driving"


class ElectricScooter(Vehicle, Chargeable):
    def __init__(self, model, max_speed):
        super().__init__(model)
        self.max_speed = max_speed

    def __str__(self):
        return f"{super().__str__()}, max speed: {self.max_speed}"

    @override
    def move(self):
        return f"{super().__str__()} is moving"

    @override
    def charge(self):
        return f"{super().__str__()} is charging"