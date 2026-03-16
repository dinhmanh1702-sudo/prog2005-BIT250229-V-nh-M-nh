class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)   # gọi constructor của lớp cha

    def sound(self):
        print("Gâu gâu")


# Chạy thử
dog1 = Dog("Lucky")

print("Tên:", dog1.name)
dog1.sound()