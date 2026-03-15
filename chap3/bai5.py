arr = list(map(float, input("Nhập danh sách số: ").split()))

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Danh sách sau khi sắp xếp:", arr)