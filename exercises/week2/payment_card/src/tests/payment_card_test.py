import unittest
from payment_card import PaymentCard

class TestPaymentCard(unittest.TestCase):
    def setUp(self):
        self.card = PaymentCard(1000)

    def test_constructor_sets_the_balance_right(self):
        # create a card with 10€/1000cents on it
        answer = str(self.card)

        self.assertEqual(answer, "The card has 10.00 euros on it")
    
    def test_eat_cheap_reduces_balance_right(self):
        self.card.eat_cheap()

        self.assertEqual(self.card.balance_in_euros(), 7.5)

    def test_eat_yummy_reduces_balance_right(self):
        self.card.eat_yummy()

        self.assertEqual(self.card.balance_in_euros(), 6.0)

    def test_eat_cheap_doesnt_make_balance_negative(self):
        card = PaymentCard(200)
        card.eat_cheap()

        self.assertEqual(card.balance_in_euros(), 2.0)

    def test_able_to_add_money(self):
        self.card.add_money(2500)

        self.assertEqual(self.card.balance_in_euros(), 35.0)

    def test_balance_does_not_exceed_maximum(self):
        self.card.add_money(20000)

        self.assertEqual(self.card.balance_in_euros(), 150.0)

    def test_eat_yummy_doesnt_make_balance_negative(self):
        card = PaymentCard(200)
        card.eat_yummy()

        self.assertEqual(card.balance_in_euros(), 2.0)

    def test_adding_negative_does_nothing(self):
        self.card.add_money(-100)

        self.assertEqual(self.card.balance_in_euros(), 10.0)

    def test_eat_cheap_makes_balance_zero(self):
        card = PaymentCard(250)
        card.eat_cheap()

        self.assertEqual(card.balance_in_euros(), 0)
    
    def test_eat_yummy_makes_balance_zero(self):
        card = PaymentCard(400)
        card.eat_yummy()

        self.assertEqual(card.balance_in_euros(), 0)