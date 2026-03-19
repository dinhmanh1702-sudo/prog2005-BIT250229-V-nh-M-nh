class Person:
    count = 0  # class variable

    def __init__(self, name, age):
        self._name = None
        self._age = None

        self.name = name  # gọi setter
        self.age = age

        Person.count += 1

    # Getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # Setter + validate (cách 1)
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Tên không hợp lệ")
        self._name = value

    # Setter + validate (cách 2)
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Tuổi phải >= 0")
        self._age = value

    # __str__
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    # Phương thức đối tượng
    def introduce(self):
        return f"Xin chào, tôi là {self.name}"

    # Class method
    @classmethod
    def get_count(cls):
        return cls.count

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Nạp chồng toán tử ==
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# Class kế thừa
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self._score = None
        self.score = score

    # Getter
    @property
    def score(self):
        return self._score

    # Setter + validate
    @score.setter
    def score(self, value):
        if value < 0 or value > 10:
            raise ValueError("Điểm phải từ 0 đến 10")
        self._score = value

    # Override __str__
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, score={self.score})"

    # Phương thức đối tượng
    def study(self):
        return f"{self.name} đang học bài"

    # Class method
    @classmethod
    def create_default(cls):
        return cls("Unknown", 18, 5)

    # Static method
    @staticmethod
    def is_pass(score):
        return score >= 5


# ================= TEST =================
p1 = Person("Mạnh", 20)
p2 = Person("Mạnh", 20)

print(p1)
print(p1.introduce())
print("So sánh:", p1 == p2)

s1 = Student("Long", 19, 8)
print(s1)
print(s1.study())

print("Số đối tượng:", Person.get_count())

print("Người lớn:", Person.is_adult(20))
print("Đậu:", Student.is_pass(8))