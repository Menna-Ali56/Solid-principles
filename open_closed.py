#open /closed principle (OCP)
#open -->foe extention(can add any method without error and don't edit any function)
#closed --> for modify (edit the code coding before but only in new class 
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price


class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.8  


class Product:
    def __init__(self, name, price, discount_strategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_price(self):
        return self.discount_strategy.apply_discount(self.price)



product1=Product("x", 200, NoDiscount())
print(product1.get_price()) #output 200
product2=Product("y", 200, SeasonalDiscount())
print(product2.get_price()) #output 160




