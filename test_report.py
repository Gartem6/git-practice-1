import unittest

from report import shipment_summary


class ShipmentSummaryTests(unittest.TestCase):
    def test_four_shipments(self):
        self.assertEqual(
            shipment_summary([8, 12, 10, 14]),
            {"count": 4, "total_pallets": 44, "average_pallets": 11.0},
        )

    def test_no_shipments(self):
        self.assertEqual(
            shipment_summary([]),
            {"count": 0, "total_pallets": 0, "average_pallets": 0},
        )

    def test_negative_pallet_count(self):
        with self.assertRaises(ValueError):
            shipment_summary([3, -1])