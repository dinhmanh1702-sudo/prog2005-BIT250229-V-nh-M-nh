m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

A = []
B = []
C = []

print("Nhập ma trận A:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("Nhập ma trận B:")
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Ma trận kết quả:")
for row in C:
    print(row)