def second_largest_sort(arr):
    if len(arr) < 2:
        return None
    unique_sorted = sorted(set(arr))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[-2]
arr = [5, 2, 8, 1, 9]
result = second_largest_sort(arr)
print(f"Второй по величине элемент: {result}")  
