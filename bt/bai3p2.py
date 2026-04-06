# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập mảng
arr = list(map(int, input("Nhập mảng: ").split()))

# Số lẻ
odd_numbers = [x for x in arr if x % 2 != 0]
print("Số lẻ:", odd_numbers, "- Số lượng:", len(odd_numbers))

# Số nguyên tố
prime_numbers = [x for x in arr if is_prime(x)]
print("Số nguyên tố:", prime_numbers)