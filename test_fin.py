import unittest

from fin import *

class FinanceTestCase(unittest.TestCase):
    def test_commercial_bank_instance(self):
        equity = Bank("Comm Bank", "Equity", False)
        self.assertIsInstance(equity, Bank, 'equity is not an instance of Fin Institution')

    def test_bank_object_type(self):
        equity = Bank("Comm Bank", "Equity", False)
        self.assertTrue(type(equity) is Bank, 'The object should be a type of Bank')

    def test_bank_name(self):
        jbb = Bank("Microfinance", "Jamii Bora Bank", False)
        self.assertEqual('Jamii Bora Bank', jbb.getname(), 'This bank should be called Jamii Bora Bank')

    def test_if_Dubai_Bank_offers_islamic_banking(self):
        db = Bank("Comm Bank", "Dubai Bank", True)
        self.assertTrue(db.offer_islamic_finance, 'Hey, Dubai Bank should offer Islamic Banking!')

    def test_equity_bank_interest(self):
        equity = CommercialBank("Comm Bank", "Equity", False, True)
        self.assertEqual(40, equity.calculate_interest(1000), 'The interest should be Ksh 40')

    def test_kwft_bank_interest(self):
        kwft = MicroFinance("Microfinance", "Kenya Women Finance Trust Bank", False, True)
        self.assertEqual(80, kwft.calculate_interest(1000), 'The interest should be Ksh 80')