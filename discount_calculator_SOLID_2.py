from dataclasses import dataclass
from abc import ABC, abstractmethod
       
class DiscountPolicy(ABC):

    @abstractmethod
    def apply_discount(self, amount) -> int:
        pass

class Nodiscount(DiscountPolicy):
        
    def apply_discount(self, amount):
        return amount

class StudentDiscount(DiscountPolicy):
    
    def apply_discount (self, amount) -> int:
        return amount *0.9
    
class VipDiscount(DiscountPolicy):
    
    def apply_discount(self, amount) -> int: 
        return amount * 0.7
    

@dataclass
class DiscountCalculator():

    policy:DiscountPolicy

    def discount_calculate(self, amount): 
        return self.policy.apply_discount(amount)
    

calc = DiscountCalculator(Nodiscount()) 
print(calc.discount_calculate(1000))