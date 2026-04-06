# Định nghĩa class Book
class Book:
    # Constructor
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Getter
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # Setter
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price


# Khởi tạo đối tượng Book
book1 = Book("Python cơ bản", 100000)

# In ra giá trị price
print("Giá sách:", book1.get_price())