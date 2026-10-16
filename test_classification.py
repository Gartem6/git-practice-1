import unittest

from classification import is_large_shipment


class LargeShipmentTests(unittest.TestCase):
    def test_below_threshold(self):
        self.assertFalse(is_large_shipment(8))

    def test_at_threshold(self):
        self.assertTrue(is_large_shipment(10))

    def test_negative_count(self):
        with self.assertRaises(ValueError):
            is_large_shipment(-1)

    def test_custom_threshold(self):
        self.assertFalse(is_large_shipment(6, threshold=7))
        self.assertTrue(is_large_shipment(7, threshold=7))