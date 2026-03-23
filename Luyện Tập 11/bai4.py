# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1. Khởi tạo danh sách
arr = list(map(int, input("Nhập danh sách số nguyên: ").split()))

# 2. Thêm phần tử
x = int(input("Nhập phần tử cần thêm: "))
arr.append(x)
print("Danh sách sau khi thêm:", arr)

# 3. Đếm số lần xuất hiện của k
k = int(input("Nhập giá trị k: "))
count = arr.count(k)
print(f"Số lần xuất hiện của {k} là:", count)

# 4. Tính tổng các số nguyên tố
tong = 0
for num in arr:
    if is_prime(num):
        tong += num
print("Tổng các số nguyên tố:", tong)

# 5. Sắp xếp danh sách
arr.sort()
print("Danh sách sau khi sắp xếp:", arr)

# 6. Xóa danh sách
arr.clear()
print("Danh sách sau khi xóa:", arr)