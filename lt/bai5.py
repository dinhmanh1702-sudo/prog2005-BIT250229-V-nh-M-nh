class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Tên hoa: {self.name}, Màu: {self.color}"

# Tạo đối tượng
f = Flower("Hoa hồng", "Đỏ")

# In thông tin
print(f)