arr = list(map(int, input("Nhập danh sách số: ").split()))

sum_even = 0

print("Các số chẵn:")
for num in arr:
    if num % 2 == 0:
        print(num)
        sum_even += num

print("Tổng các số chẵn:", sum_even)