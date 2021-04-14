class Building:
    def __init__(self, name_build, over, height, sqare, city):
        self.name_build = name_build
        self.over = over
        self.height = height
        self.sqare = sqare
        self.city = city

    def __str__(self) -> str:
        return ' '.join([self.__name_build, self.__over, self.__height, self.__sqare, self.__city])

    @property
    def name_build(self):
        return self.__name_build

    @name_build.setter
    def name_build(self, value):
        if value.istitle():
            self.__name_build = value
        else:
            raise ValueError("Incorrect name")

    @name_build.getter
    def name_build(self):
        return self.__name_build

    @name_build.deleter
    def name_build(self, k):
        del k.__name_build

    @property
    def over(self):
        return self.__over

    @over.setter
    def over(self, value: int):
        if isinstance(value(int, float)):
            self.__over = value
        else:
            raise ValueError("value must be a number")

    @over.getter
    def over(self):
        return self.__over

    @over.deleter
    def over(self, d):
        del d.__over

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value(int, float)):
            self.__height = value
        else:
            raise ValueError("value must be a number")

    @height.getter
    def height(self):
        return self.__height

    @height.deleter
    def height(self, w):
        del w.__height

    @property
    def square(self):
        return self.square

    @square.setter
    def square(self, value):
        if isinstance(value(int, float)):
            self.__square = value
        else:
            raise ValueError("value must be a number")

    @square.getter
    def sqare(self):
        return self.__square

    @sqare.deleter
    def sqare_(self, d):
        del d.__sqare

    @property
    def city(self):
        return self.city

    @city.setter
    def city(self, value: str):
        if value in ('Kyiv', 'Lviv', 'Dnipro'):
            self.__city = value
        else:
            raise ValueError("City must be: Kyiv, Lviv or Dnipro")

    @city.getter
    def sqare(self):
        return self.__square

    @city.deleter
    def sqare_(self, d):
        del d.__sqare

if __name__ == "__main__":
    test = Building("house", 10, 20, 75, 'Kyiv')
    print(test)
