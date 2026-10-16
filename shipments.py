def average_pallets(pallet_counts):
    if not pallet_counts:
        return 0
    return sum(pallet_counts) / len(pallet_counts)