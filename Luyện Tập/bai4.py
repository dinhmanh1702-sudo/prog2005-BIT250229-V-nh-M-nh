s = input("Chuỗi: ")

upper = lower = digit = special = space = vowel = consonant = 0

vowels = "aeiouAEIOU"

for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

    if char.isdigit():
        digit += 1

    if char.isspace():
        space += 1

    if char.isalpha():
        if char in vowels:
            vowel += 1
        else:
            consonant += 1

    if not char.isalnum() and not char.isspace():
        special += 1

print("M:", upper)
print("m:", lower)
print("1:", digit)
print("@:", special)
print(" :", space)
print("-2:", vowel)
print(".:", consonant)