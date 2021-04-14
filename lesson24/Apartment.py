class Apartment:
    def __init__(self, num_apart, peoples, height, sqare):
        self.num_apart = num_apart
        self.peoples = peoples
        self.height = height
        self.sqare = sqare

    @property
    def num_apart(self):
        return self.__num_apart

    @num_apart.setter
    def num_apart(self, value):
     self.__num_apart = value

    @property
    def peoples(self):
        return self.__peoples

    @peoples.setter
    def peoples(self, value):
        self.__peoples = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__heihgt = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value


if __name__ == "__main__":
    test = Apartment(10, 5, 8, 7)
    print(test)
