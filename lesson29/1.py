
import json
from threading import Thread


def open_json(data):
    pass

def positive_num(data):
    print(f"{data}">0)

def negative_num(data):
    print(f"{data}"<0)

if __name__ == "__main__":
    while True:
        open_json()
        t = Thread(target=positive_num, args=(data, ))
        t.start()

        t1 = Thread(target=negative_num, args=(data,))
        t1.start()
