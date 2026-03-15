arr = list(map(int, input("Nhập danh sách số: ").split()))

for num in arr:
    if num > 10:
        print("Số đầu tiên lớn hơn 10:", num)
        break
else:
    print("Không có số nào lớn hơn 10")