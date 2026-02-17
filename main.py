from abc import ABC, abstractmethod
from typing_extensions import override
from vehicles import Vehicle, ElectricCar, ElectricScooter






electri1 = ElectricCar("tesla 3", 2)
print(electri1)
print(electri1.move())
print(electri1.charge())
print(electri1.drive())

electri_scooter1 = ElectricScooter("expeng p7", 200)
print(electri_scooter1)
print(electri_scooter1.move())
print(electri_scooter1.charge())