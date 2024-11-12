import unittest
from payment_card import PaymentCard
from cash_register import CashRegister

class TestPaymentCard(unittest.TestCase):
    def setUp(self):
        self.register = CashRegister()
        self.card = PaymentCard(1000)

    def test_initial_values(self):
        self.assertEqual(self.register.money, 100000)
        self.assertEqual(self.register.cheap, 0)
        self.assertEqual(self.register.yummy, 0)

    def test_eat_cheap_with_cash_sufficient_payment(self):
        change = self.register.eat_cheap_with_cash(300)

        self.assertEqual(self.register.money, 100240)
        self.assertEqual(change, 60)
        self.assertEqual(self.register.cheap, 1)

    def test_eat_yummy_with_cash_sufficient_payment(self):
        change = self.register.eat_yummy_with_cash(500)

        self.assertEqual(self.register.money, 100400)
        self.assertEqual(change, 100)
        self.assertEqual(self.register.yummy, 1)

    def test_eat_cheap_with_cash_insufficient_payment(self):
        change = self.register.eat_cheap_with_cash(200)

        self.assertEqual(self.register.money, 100000)
        self.assertEqual(change, 200)
        self.assertEqual(self.register.cheap, 0)

    def test_eat_yummy_with_cash_insufficient_payment(self):
        change = self.register.eat_yummy_with_cash(300)

        self.assertEqual(self.register.money, 100000)
        self.assertEqual(change, 300)
        self.assertEqual(self.register.yummy, 0)

    def test_eat_cheap_with_card_sufficient_balance(self):
        success = self.register.eat_cheap_with_card(self.card)

        self.assertTrue(success)
        self.assertEqual(self.card.balance, 760)
        self.assertEqual(self.register.cheap, 1)

    def test_eat_yummy_with_card_sufficient_balance(self):
        success = self.register.eat_yummy_with_card(self.card)

        self.assertTrue(success)
        self.assertEqual(self.card.balance, 600)
        self.assertEqual(self.register.yummy, 1)

    def test_eat_cheap_with_card_insufficient_balance(self):
        card = PaymentCard(100)
        success = self.register.eat_cheap_with_card(card)

        self.assertFalse(success)
        self.assertEqual(card.balance, 100)
        self.assertEqual(self.register.cheap, 0)

    def test_eat_yummy_with_card_insufficient_balance(self):
        card = PaymentCard(200)
        success = self.register.eat_yummy_with_card(card)

        self.assertFalse(success)
        self.assertEqual(card.balance, 200)
        self.assertEqual(self.register.yummy, 0)

    def test_cash_does_not_change_with_card_payment(self):
        cash = self.register.money
        self.register.eat_cheap_with_card(self.card)

        self.assertEqual(self.register.money, cash)

        self.register.eat_yummy_with_card(self.card)

        self.assertEqual(self.register.money, cash)

    def test_add_money_to_card(self):
        self.register.add_money_to_card(self.card, 500)

        self.assertEqual(self.card.balance, 1500)
        self.assertEqual(self.register.money, 100500)
    
    def test_add_negative_money_to_card(self):
        self.register.add_money_to_card(self.card,-100)

        self.assertEqual(self.register.money, 100000)
        self.assertEqual(self.card.balance, 1000)
    
    def test_money_in_euros(self):
        self.assertEqual(self.register.money_in_euros(), 1000)

if __name__ == '__main__':
    unittest.main()
