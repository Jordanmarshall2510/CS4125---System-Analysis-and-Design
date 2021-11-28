from abc import abstractmethod
from datetime import datetime


class ElectricityGenerator:
    @abstractmethod
    def update(self, date: datetime) -> int:
        '''Method to update the electricity generated at a specific date'''
        pass

    @abstractmethod
    def get_electricity_generated() -> int:
        '''Method to get the electricity generated by a generator'''
        pass

    @staticmethod
    @abstractmethod
    def generate_generators(count: int) -> list:
        '''Static method to generate a specific type of generator'''
        pass
