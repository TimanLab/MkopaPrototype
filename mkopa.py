from ast import And
from calendar import month
from operator import truediv
from time import time
from timeit import timeit
#from typing_extensions import Self


class MLoan:

    interest = 0.2
    months = 12
    time = 1440
    deposit = ''

    def __init__(self, deposit, quantity, time):

        #This asserts that the prices and quantities are actually decimal numbers and not strings
        assert deposit is float
        assert quantity is int
        assert time is timeit
        #Initialise the above         
        self.deposit = deposit
        self.quantity = quantity
        self.time = time
    print("Dear client please enter your deposit amount " + deposit)
   
class phones(MLoan):
    def Brands(self, brand, price=0, quantity=0):
        assert price is float
        assert quantity is int

        self.brand = brand
        self.price = price
        self.quantity = quantity

    item1 = Brands("Samsung", 25000, 50)
    item2 = Brands("Sony", 20000, 20)
    item3 = Brands("Iphone", 50000, 10)

   # print(f"dear client please enter your preferred phone brand "+ {brand} + "\n The value of your brand is "+ {price})

    def totals(self):
        self.quantity = 1
        self.months -= 1

        #what is the grand total of customers deposit vis a vis time?
        self.time = self.time
        return self.deposit * self.interest

        

    def fully_paid(self):
        if self.totals() == (self.price(phones) * self.interest):
            self.time = time
            self.months = month
            return True
            
        else:
            self.time -= 1
            return self.partial_pay()
                   
    @property
    def partial_pay(self):
        self.months = 12
        self.time -= 1
        if self.totals() != self.fully_paid():
            #return True
            while True:
                self.totals() + self.interest
                self.months -= 1
                for i in smonths:
                    print(
                        f"Dear client, your new phone price is {self.totals} to be paid over a period of {i}")
        else:
            return self.fully_paid()

    def blocked(self):
        self.months = 12
        if self.partial_pay() != self.price(phones) * self.interest:
            #return True
            while True:
                self.time += 1
                self.months += 1
                return self.price(phones) - (self.totals() * self.interest)
                for i in months:
                    print(f"Dear client your phone was blocked due to late payments, kindly pay {i} deposit to unlock")
        else:
            self.time -= 1
            self.months -=1
            return self.partial_pay()

    def balance(self):
        self.months -= 1
        return self.price(phones) * self.interest - self.totals()

