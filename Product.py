from typing import Iterator

class Product:
    def __init__(self, name_prod, price):
        self.name_prod = name_prod
        self.price = price

    def creator_prod(self, name_prod, price):
        return dict((name_prod) + (price))

class Basket(Product):

    def __iter__(self):
        print(self.__name_prod.values())
        return iter(self.__name_prod.values())

    def __getitem__(self, key):
        return self.__name_prod[key]

if __name__ == "__main__":
    basket = Basket({water:45, meat: 47})
    for p in basket:
        print(p)
