n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - i - 1:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()