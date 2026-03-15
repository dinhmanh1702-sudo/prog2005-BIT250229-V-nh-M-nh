def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


text = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(text))