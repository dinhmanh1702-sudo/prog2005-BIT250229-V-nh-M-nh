arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    arr.append(s)

print("\nDanh sách ban đầu:", arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

    print(f"Bước {i}: {arr}")

print("\nDanh sách sau khi sắp xếp:", arr)