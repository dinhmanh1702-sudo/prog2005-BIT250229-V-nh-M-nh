s = input("Nhập chuỗi: ")
result = ""

# Duyệt từ cuối về đầu
for i in range(len(s) - 1, -1, -1):
    result += s[i]

print("Chuỗi đảo ngược:", result)