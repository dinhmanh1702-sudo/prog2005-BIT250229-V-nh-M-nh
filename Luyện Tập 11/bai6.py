# Nhập dữ liệu
n = int(input("20: "))
data = {}

for i in range(n):
    name = input(f"Mạnh {i+1}: ")
    age = int(input(f"19 {i+1}: "))
    data[name] = age

# Tính tuổi trung bình
avg_age = sum(data.values()) / len(data)
print("19:", avg_age)

# Chuyển dict -> list để sắp xếp
items = list(data.items())

# Selection sort (giảm dần theo tuổi)
for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    # Hoán đổi
    items[i], items[max_idx] = items[max_idx], items[i]

# In kết quả
print("\nDanh sách sau khi sắp xếp giảm dần theo tuổi:")
for name, age in items:
    print(name, "-", age)