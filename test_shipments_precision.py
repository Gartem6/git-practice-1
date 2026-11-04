import unittest

from shipments import average_pallets


class AveragePalletsPrecisionTests(unittest.TestCase):
    def test_fractional_average(self):
        self.assertEqual(average_pallets([1, 2]), 1.5)