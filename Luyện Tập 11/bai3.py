# Nhập danh sách số (cách nhau bởi dấu cách)
nums = list(map(int, input("20,30,40,50,60: ").split()))

tong = 0

print("20,30:")
for n in nums:
    if n % 2 == 0:
        print(n, end=" ")
        tong += n

print("\nTổng các số chẵn là:", tong)