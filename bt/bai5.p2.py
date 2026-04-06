# Ghi file
with open("books.txt", "w", encoding="utf-8") as f:
    f.write("Book 1;30000\n")
    f.write("Book 2;50000\n")
    f.write("Book 3;100000\n")
    f.write("Tong;900000\n")

print("Đã ghi file thành công!")