import unittest

from shipments import max_pallets


class MaxPalletsTests(unittest.TestCase):
    def test_maximum_pallet_count(self):
        self.assertEqual(max_pallets([8, 12, 14, 10]), 14)

    def test_empty_shipments(self):
        self.assertEqual(max_pallets([]), 0)

    def test_negative_pallet_count(self):
        with self.assertRaises(ValueError):
            max_pallets([8, -1])