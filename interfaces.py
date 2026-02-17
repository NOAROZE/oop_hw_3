from abc import ABC, abstractmethod

class Chargeable(ABC):
    @abstractmethod
    def charge(self):
        pass


class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass