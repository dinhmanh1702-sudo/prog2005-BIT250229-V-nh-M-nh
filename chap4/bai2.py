def diem_trung_binh(ds):
    tong = sum(ds.values())
    so_sv = len(ds)
    return tong / so_sv

sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Cuong": 9
}

print("Điểm trung bình:", diem_trung_binh(sinh_vien))