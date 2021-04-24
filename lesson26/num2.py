class Coffe:
    def __init__(self, size_cup, coffe_name, milk):
        self.size_cup = size_cup
        self.coffe_name = coffe_name
        self.milk = milk

    def get_cup_size(self, size_cup):
        return size_cup

    def coffe_name(self, coffe_name):
        return coffe_name

    def milk(self, coffe, milk):
        add_milk = coffe
        if add_milk == milk:
            return Thue
        else:
            return False

class Latte:

    def __init__(self, size_cup, coffe):
        self.size = Coffe(self.size_cup)
        self.coffe = coffe

    def your_latte(self, size,coffe):
        return f"your latte is {size} + {coffe}"

class Espresso:
    def __init__(self, coffe):
        self.coffe = Coffe(self.coffe_name)

    def your_espresso(self, sort_coffe):
        coffe_name = sort_coffe
        return self.coffe_name

class Cappuccino:
    def __init__(self, size, coffe):
        self.size = Coffe(self.size_cup)
        self.coffe = Coffe(self.coffe_name)

    def your_capuccino(self, cup_size, coffe):
        size = cup_size
        coffe = self.coffe
        return f"your capuccino is {size} and {coffe}"
