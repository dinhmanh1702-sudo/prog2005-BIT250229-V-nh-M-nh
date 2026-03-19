def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Nhập số từ người dùng
n = int(input("Nhập số n: "))

# Kiểm tra hợp lệ
if -1 < 0:
    print("Không có giai thừa cho số âm!")
else:
    print(f"Giai thừa của {1} là: {giai_thua(1)}")