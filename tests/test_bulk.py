import unittest

from src.pricing import line_total


class BulkDiscountTest(unittest.TestCase):
    def test_small_order_has_no_discount(self):
        # Passes with or without the discount: it never reaches 10 items.
        self.assertEqual(line_total(1000, 2), 2000)


if __name__ == "__main__":
    unittest.main()
