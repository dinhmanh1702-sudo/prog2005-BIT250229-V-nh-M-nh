colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except ValueError:
    print("Green không có trong danh sách")

print("Danh sách sau khi xóa:", colors)