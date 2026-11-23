import unittest

from src.pricing import line_total


class BulkDiscountTest(unittest.TestCase):
    def test_small_order_has_no_discount(self):
        self.assertEqual(line_total(1000, 2), 2000)

    def test_ten_items_get_ten_percent_off(self):
        self.assertEqual(line_total(1000, 10), 9000)


if __name__ == "__main__":
    unittest.main()
