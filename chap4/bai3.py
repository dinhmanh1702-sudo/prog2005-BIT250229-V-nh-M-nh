def kiem_tra_key(d, key):
    if key in d:
        print("Key tồn tại")
    else:
        print("Key không tồn tại")

data = {"a": 1, "b": 2, "c": 3}

kiem_tra_key(data, "b")