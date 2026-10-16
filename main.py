from shipments import average_pallets

pallet_counts = [8, 12, 10, 14]
result = average_pallets(pallet_counts)
print(f"Среднее количество паллет на одну отгрузку: {result}")
print(f"Количество отгрузок: {len(pallet_counts)}")