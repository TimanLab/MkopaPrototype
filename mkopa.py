from calendar import month
from operator import truediv


class Mkopa:

    interest = 0.2
    months = 12

    def __init__(self, price, quantity, period):

        #This asserts that the prices and quantities are actually decimal numbers and not strings
        assert price is float
        assert quantity is int
        #Initialise the above         
        self.price = price
        self.quantity = quantity
        self.period = period
    
    def totals(self):
        return self.price * self.quantity

    def fully_paid(self):
        if self.totals == self.totals:
            return True
        else:
            return False

    @property
    def partial_pay(self):
        self.months = 11
        if self.totals != self.totals:
            return True
            while True:
                return self.totals == self.totals + (self.totals * self.interest)
                self.months -= 1
                for i in months:
                    print(
                        f"Dear client, your new phone price is {self.totals} to be paid over a period of {i}")
        else:
            return self.fully_paid

    def blocked(self):
        self.months = 11
        if self.totals != self.totals and not self.partial_pay:
            return True
            while True:
                return self.totals * self.interest
                self.months += 1
                for i in months:
                    print(f"Dear client your phone was blocked due to late payments, kindly pay {i} deposit to unlock")
        else:
            return self.partial_pay