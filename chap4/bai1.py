def tinh_toan(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)

    return tong, lon_nhat, nho_nhat


# Ví dụ
data = (3, 7, 2, 9, 5)
kq = tinh_toan(data)

print("Tổng:", kq[0])
print("Lớn nhất:", kq[1])
print("Nhỏ nhất:", kq[2])