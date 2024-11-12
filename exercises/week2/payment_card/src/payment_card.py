# Prices are in cents
CHEAP = 250
YUMMY = 400


class PaymentCard:
    def __init__(self, balance):
        # The balance is in cents
        self.balance = balance

    def eat_cheap(self):
        if self.balance >= CHEAP:
            self.balance -= CHEAP

    def eat_yummy(self):
        if self.balance >= YUMMY:
            self.balance -= YUMMY

    def add_money(self, amount):
        if amount < 0:
            return

        self.balance += amount

        if self.balance > 15000:
            self.balance = 15000
    
    def balance_in_euros(self):
        return self.balance / 100

    def __str__(self):
        balance_in_euros = round(self.balance / 100, 2)

        return "The card has {:0.2f} euros on it".format(balance_in_euros)
