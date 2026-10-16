import unittest

from shipments import average_pallets


class AveragePalletsTests(unittest.TestCase):
    def test_three_shipments(self):
        self.assertEqual(average_pallets([2, 5, 8]), 5)

    def test_empty_list(self):
        self.assertEqual(average_pallets([]), 0)