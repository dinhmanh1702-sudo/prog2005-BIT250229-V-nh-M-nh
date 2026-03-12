bai1

a = 10
b = 4

result = (a**2 + b**2) / (a - b)

print("Kết quả:", result)

bai2

import math

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

print("Lũy thừa a^b:", a ** b)

print("Căn bậc 2 của a:", math.sqrt(a))
print("Căn bậc 2 của b:", math.sqrt(b))

print("Chia lấy phần nguyên a//b:", a // b)
print("Chia lấy phần dư a%b:", a % b)

print("Làm tròn a:", round(a))
print("Làm tròn b:", round(b))

bai3

n = int(input("Nhập số từ 1 đến 9: "))

for i in range(1, 10):
    print(n, "x", i, "=", n * i)

bai4

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)

bai5

import random

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)

r = int(input("Nhập hàng cần hiển thị: "))
print("Hàng", r, ":", matrix[r-1])

c = int(input("Nhập cột cần hiển thị: "))
column = []
for i in range(m):
    column.append(matrix[i][c-1])
print("Cột", c, ":", column)

max_value = matrix[0][0]
for row in matrix:
    for val in row:
        if val > max_value:
            max_value = val

print("Giá trị lớn nhất:", max_value)

bai6

import math

s = input("Nhập chuỗi số: ")

numbers = [int(x.strip()) for x in s.split(";")]

for num in numbers:
    print(num)

even = 0
negative = 0
prime = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for num in numbers:
    if num % 2 == 0:
        even += 1
    if num < 0:
        negative += 1
    if is_prime(num):
        prime += 1

avg = sum(numbers) / len(numbers)

print("Số chẵn:", even)
print("Số âm:", negative)
print("Số nguyên tố:", prime)
print("Trung bình:", avg)

bai7

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("A", 10)
s2 = Student("B", 8)

bai8

class Student:
    def __init__(self, name, score):
        if 0 <= score <= 10:
            self.name = name
            self.score = score
        else:
            print("Điểm không hợp lệ")

bai9

class Student:
    def __init__(self, name, score):
        if 0 <= score <= 10:
            self.name = name
            self.score = score
        else:
            print("Điểm không hợp lệ")

    def display(self):
        print("Sinh viên", self.name, "có điểm là", self.score)

s1 = Student("A", 10)
s2 = Student("B", 8)

s1.display()
s2.display()

bai10

code = input("Nhập mã sản phẩm: ")
name = input("Nhập tên sản phẩm: ")
price = input("Nhập giá: ")

with open("products.txt", "a") as file:
    file.write(code + ";" + name + ";" + price + "\n")

print("Đã lưu sản phẩm vào file")