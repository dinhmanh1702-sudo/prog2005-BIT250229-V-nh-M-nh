import csv
import os

# Nhập dữ liệu
n = int(input("Nhập số nhân viên: "))
employees = []

for i in range(n):
    print(f"\nNhân viên {i + 1}:")
    name = input("Tên: ")
    age = input("Tuổi: ")
    emp_id = input("ID: ")

    employees.append([name, age, emp_id])

# ------------------ Lưu file TXT ------------------
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    for emp in employees:
        f.write(f"Tên: {emp[0]}, Tuổi: {emp[1]}, ID: {emp[2]}\n")

# ------------------ Lưu file CSV ------------------
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])  # header
    writer.writerows(employees)

print("\nĐã lưu file nhanvien.txt và nhanvien.csv")

# ------------------ Hiển thị nội dung file ------------------
print("\nNội dung file TXT:")
with open("nhanvien.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("Nội dung file CSV:")
with open("nhanvien.csv", "r", encoding="utf-8") as f:
    print(f.read())

# ------------------ Mở file để chụp màn hình ------------------
print("\nĐang mở file để bạn chụp ảnh...")
os.startfile("nhanvien.txt")
os.startfile("nhanvien.csv")