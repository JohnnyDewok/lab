import unittest
from account import *

class MyTestCase(unittest.TestCase):
    delta_value = 0.001

    def setUp(self):
        self.p1 = Account('001-Dean')
        self.p2 = Account('101-Daisy')

    def tearDown(self):
        del self.p1
        del self.p2

    def test_init(self):
        self.assertEqual(self.p1.get_name(), '001-Dean')
        self.assertEqual(self.p2.get_name(), '101-Daisy')

        self.assertAlmostEqual(self.p1.get_balance(), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.get_balance(), 0, delta=self.delta_value)

    def test_deposit(self):
        self.p1.deposit(10)
        self.assertAlmostEqual(self.p1.get_balance(), 10, delta=self.delta_value)

        self.p2.deposit(10)
        self.assertAlmostEqual(self.p2.get_balance(), 10, delta=self.delta_value)

        self.p1.deposit(-10)
        self.assertAlmostEqual(self.p1.get_balance(), 10, delta=self.delta_value)

        self.p2.deposit(-10)
        self.assertAlmostEqual(self.p2.get_balance(), 10, delta=self.delta_value)

        self.p1.deposit(0)
        self.assertAlmostEqual(self.p1.get_balance(), 10, delta=self.delta_value)

        self.p2.deposit(0)
        self.assertAlmostEqual(self.p2.get_balance(), 10, delta=self.delta_value)

        self.assertTrue(self.p1.deposit(1))
        self.assertFalse(self.p1.deposit(-1))

    def test_withdraw(self):
        self.assertAlmostEqual(self.p1.get_balance(), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.get_balance(), 0, delta=self.delta_value)

        self.assertAlmostEqual(self.p1.withdraw(10), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(10), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p1.withdraw(0), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(0), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p1.withdraw(-10), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(-10), 0, delta=self.delta_value)

        self.p1.deposit(10)
        self.p2.deposit(10)

        self.assertAlmostEqual(self.p1.withdraw(10), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(5), 5, delta=self.delta_value)

        self.assertTrue(self.p1.withdraw(1))
        self.assertFalse(self.p1.withdraw(-1))
        self.assertFalse(self.p1.withdraw(11))


if __name__ == '__main__':
    unittest.main()
