def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test
ds = [5, 2, 9, 1, 3]
print("Sau khi sắp xếp:", bubble_sort(ds))