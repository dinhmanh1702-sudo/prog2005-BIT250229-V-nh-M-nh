arr = list(map(int, input("Nhập danh sách số: ").split()))

print("Các số lẻ:")
for num in arr:
    if num % 2 != 0:
        print(num)