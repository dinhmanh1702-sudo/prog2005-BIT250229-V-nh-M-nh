class Book:
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


# Tạo đối tượng
book = Book("Python", 50000)

# In price
print("Giá sách:", book.get_price())