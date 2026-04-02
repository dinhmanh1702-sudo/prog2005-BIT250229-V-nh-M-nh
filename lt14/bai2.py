n = int(input("Nhập n: "))
for i in range(n):
    print("*  " * n)

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print("*  " * i)

n = int(input("Nhập n: "))
for i in range(n, 0, -1):
    print("*  " * i)

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print("   " * (n - i) + "*  " * i)

n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()

n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

n = int(input("Nhập n: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        if i == j:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()