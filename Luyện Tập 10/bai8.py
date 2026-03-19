# Nhập 5 chuỗi
arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    arr.append(s)

n = len(arr)

print("\nBắt đầu sắp xếp...\n")

# Bubble Sort (giảm dần theo độ dài)
for i in range(n):
    for j in range(0, n - i - 1):
        # So sánh độ dài
        if len(arr[j]) < len(arr[j + 1]):
            # Hoán đổi
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # In từng bước
        print(f"Bước {i}-{j}: {arr}")

print("\nKết quả cuối cùng:")
for s in arr:
    print(s, "(độ dài:", len(s), ")")