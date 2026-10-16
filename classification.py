def is_large_shipment(pallet_count, threshold=10):
    """Определяет, достигла ли отгрузка порога по числу паллет."""
    if pallet_count < 0:
        raise ValueError("Количество паллет не может быть отрицательным")
    return pallet_count >= threshold