def nhap_ma_tran(m, n, ten):
    ma_tran = []
    print(f"\nNhập ma trận {ten}:")

    for i in range(m):
        hang = []
        for j in range(n):
            while True:
                gia_tri = input(f"Nhập phần tử [{i}][{j}]: ")

                if gia_tri.strip() == "":
                    print("❌ Lỗi: Không được nhập rỗng!")
                    continue

                try:
                    hang.append(float(gia_tri))
                    break
                except:
                    print("❌ Lỗi: Vui lòng nhập số hợp lệ!")

        ma_tran.append(hang)

    return ma_tran


def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])

    C = []
    for i in range(m):
        hang = []
        for j in range(n):
            hang.append(A[i][j] + B[i][j])
        C.append(hang)

    return C


def in_ma_tran(M):
    for hang in M:
        print(hang)


# ===== CHƯƠNG TRÌNH CHÍNH =====
while True:
    try:
        m = int(input("Nhập số hàng: "))
        n = int(input("Nhập số cột: "))

        if m <= 0 or n <= 0:
            print("❌ Kích thước phải > 0")
            continue
        break
    except:
        print("❌ Nhập số nguyên hợp lệ!")

# Nhập 2 ma trận
A = nhap_ma_tran(m, n, "A")
B = nhap_ma_tran(m, n, "B")

# Cộng ma trận
C = cong_ma_tran(A, B)

# In kết quả
print("\nMa trận A:")
in_ma_tran(A)

print("\nMa trận B:")
in_ma_tran(B)

print("\nMa trận tổng C:")
in_ma_tran(C)