def average_pallets(pallet_counts):
    """Возвращает среднее число паллет на отгрузку."""
    if not pallet_counts:
        return 0
    if any(count < 0 for count in pallet_counts):
        raise ValueError("Количество паллет не может быть отрицательным")
    total_pallets = sum(pallet_counts)
    return total_pallets / len(pallet_counts)

def max_pallets(pallet_counts):
    """Возвращает максимальное число паллет среди отгрузок.

    Для пустого списка возвращает 0.
    При отрицательном количестве паллет вызывает ValueError.
    """
    if any(count < 0 for count in pallet_counts):
        raise ValueError("Количество паллет не может быть отрицательным")
    return max(pallet_counts, default=0)