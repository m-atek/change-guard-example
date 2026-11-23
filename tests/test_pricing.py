import unittest

from src.pricing import line_total, order_total


class PricingTest(unittest.TestCase):
    def test_line_total(self):
        self.assertEqual(line_total(250, 2), 500)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            line_total(250, -1)

    def test_order_total(self):
        self.assertEqual(order_total([(100, 1), (250, 2)]), 600)


if __name__ == "__main__":
    unittest.main()
