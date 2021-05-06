class Myrange:

    def __init__(self, num, stop) -> None:
        self.__num = num
        self.__stop = stop

    def __iter__(self):
        return self

    def __next__(self):

        if self.__stop <=0:
            raise StopIteration
        self.__num = self.__num ** 2
        self.__stop = self.__stop - 1
        return self.__num

if __name__ == "__main__":
    num = Myrange(6,8)
    for elem in num:
        print(elem)
