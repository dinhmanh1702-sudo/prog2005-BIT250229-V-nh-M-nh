class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    # getter/setter + validate
    @property
    def name(self): return self._name

    @name.setter
    def name(self, value):
        if not value: raise ValueError("Tên rỗng")
        self._name = value

    @property
    def age(self): return self._age

    @age.setter
    def age(self, value):
        if value < 0: raise ValueError("Tuổi sai")
        self._age = value

    def __str__(self):
        return f"{self.name}-{self.age}"

    def greet(self):
        return f"Hi {self.name}"

    @classmethod
    def total(cls):
        return cls.count

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


class Student(Person):  # kế thừa
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    @property
    def score(self): return self._score

    @score.setter
    def score(self, value):
        if not (0 <= value <= 10):
            raise ValueError("Điểm sai")
        self._score = value

    def __str__(self):
        return f"{self.name}-{self.age}-{self.score}"

    def study(self):
        return "Studying"

    @classmethod
    def default(cls):
        return cls("A", 18, 5)

    @staticmethod
    def pass_score(s):
        return s >= 5