def find_index_builtin(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1
arr = [2, 4, 7, 1, 9]
target = 7
result = find_index_builtin(arr, target)
print(f"Индекс числа {target}: {result}") 
