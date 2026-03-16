class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    # Nạp chồng toán tử ==
    def __eq__(self, other):
        return self.diem == other.diem


# Chạy thử
sv1 = SinhVien(8)
sv2 = SinhVien(8)
sv3 = SinhVien(9)

print(sv1 == sv2)  # True
print(sv1 == sv3)  # False