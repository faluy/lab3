def even_indices_slice(arr):
    return arr[::2]
arr = [10, 20, 30, 40, 50]
result = even_indices_slice(arr)
print(f"Элементы с четными индексами: {result}")
