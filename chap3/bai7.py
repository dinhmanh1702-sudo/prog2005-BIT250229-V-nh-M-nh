arr = list(map(int, input("Nhập danh sách số: ").split()))
x = int(input("Nhập số cần tìm: "))

index = -1

for i in range(len(arr)):
    if arr[i] == x:
        index = i
        break

if index != -1:
    print("Tìm thấy tại vị trí:", index)
else:
    print("Không tìm thấy")