import os

def lay_ten_file(path):
    return os.path.basename(path)

def lay_ten_khong_duoi(path):
    return os.path.splitext(os.path.basename(path))[0]

# Test
path = "d:\\music\\muabui.mp3"
print(lay_ten_file(path))       # muabui.mp3
print(lay_ten_khong_duoi(path)) # muabui