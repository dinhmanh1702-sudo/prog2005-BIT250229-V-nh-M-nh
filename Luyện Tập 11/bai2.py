def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # So sánh theo độ dài (giảm dần)
        if len(arr[mid]) == len(target):
            # Nếu độ dài bằng thì so sánh nội dung
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1

        elif len(arr[mid]) < len(target):
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Nhập 5 chuỗi (đã sắp xếp sẵn theo bài trước)
arr = []
print("Nhập 5 chuỗi (đã sắp xếp giảm dần theo độ dài):")
for i in range(5):
    s = input(f"Chuỗi {i + 1}: ")
    arr.append(s)

# Nhập chuỗi cần tìm
target = input("Nhập chuỗi cần tìm: ")

# Tìm kiếm
result = binary_search(arr, target)

# In kết quả
if result != -1:
    print(f"Tìm thấy tại vị trí: {result}")
else:
    print("Không tìm thấy chuỗi!")