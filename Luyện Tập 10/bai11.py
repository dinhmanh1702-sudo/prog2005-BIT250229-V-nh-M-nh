while True:
    print("\n--- MENU ---")
    print("1. Facebook (Mk:1234)")
    print("2. TikTok (Mk:5678)")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        # Bài 7
        while True:
            pwd = input("Nhập mật khẩu: ")
            if pwd == "python123":
                print("Đúng!")
                break
            else:
                print("Sai, nhập lại!")

    elif choice == "2":
        # Bài 8
        arr = [input(f"Chuỗi {i+1}: ") for i in range(5)]

        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if len(arr[j]) < len(arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    print(arr)

    elif choice == "0":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ!")