# Khởi tạo dictionary
my_dict = {}

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập key - value
for i in range(n):
    key = input(f"Nhập key {i+1}: ")
    value = input(f"Nhập value {i+1}: ")
    my_dict[key] = value

# Nhập key cần kiểm tra
k = input("Nhập key cần kiểm tra: ")

# Kiểm tra
if k in my_dict:
    print("Key tồn tại trong dictionary!")
else:
    print("Key không tồn tại!")