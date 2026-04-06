# Nhập danh sách
names = []
for i in range(5):
    name = input(f"Nhập tên người thứ {i+1}: ")
    names.append(name)

print("Danh sách ban đầu:", names)

# Xóa người thứ 2 (index = 1)
del names[1]

print("Danh sách sau khi xóa:", names)