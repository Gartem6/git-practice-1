from shipments import average_pallets


def shipment_summary(pallet_counts):
    return {
        "count": len(pallet_counts),
        "total_pallets": sum(pallet_counts),
        "average_pallets": average_pallets(pallet_counts),
    }