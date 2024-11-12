import unittest
from payment_card import PaymentCard

class TestPaymentCard(unittest.TestCase):
    def setUp(self):
        self.card = PaymentCard(1000)

    def test_card_exists(self):
        self.assertNotEqual(self.card, None)

    def test_initial_balance_correct(self):
        self.assertEqual(self.card.balance, 1000)

    def test_adding_money_increases_balance(self):
        self.card.add_money(500)

        self.assertEqual(self.card.balance, 1500)
    
    def test_taking_money_decreases_balance_correct(self):
        self.card.take_money(500)

        self.assertEqual(self.card.balance, 500)

    def test_taking_too_much_does_not_change_balance(self):
        self.card.take_money(1200)

        self.assertEqual(self.card.balance, 1000)

    def test_taking_money_returns_true_if_enough(self):
        taking = self.card.take_money(300)

        self.assertEqual(taking, True)
    
    def test_taking_money_returns_false_if_not_enough(self):
        taking = self.card.take_money(1100)

        self.assertEqual(taking, False)

    def test_balance_in_euros_works(self):
        self.assertEqual(self.card.balance_in_euros(), 10.0)
    
    def test_string_representation_is_correct(self):
        self.assertEqual(str(self.card), "The card has 10.00 euros on it")