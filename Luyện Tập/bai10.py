class SinhVien:
    count = 0

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1

    @classmethod
    def dem_sinh_vien(cls):
        return cls.count


# Chạy ví dụ
sv1 = SinhVien(7)
sv2 = SinhVien(8)
sv3 = SinhVien(9)

print("Số sinh viên đã tạo:", SinhVien.dem_sinh_vien())