def average_pallets(pallet_counts):
    if not pallet_counts:
        return 0
    if any(count < 0 for count in pallet_counts):
        raise ValueError("Количество паллет не может быть отрицательным")
    total_pallets = sum(pallet_counts)
    return total_pallets / len(pallet_counts)