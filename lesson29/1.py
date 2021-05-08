
import json
from threading import Thread


def open_json(data):
    pass

def odd_num(data):
    print(f"{data}">0)

def even_num(data):
    print(f"{data}"<0)

if __name__ == "__main__":
    while True:
        open_json()
        t = Thread(target=odd_num, args=(data, ))
        t.start()

        t1 = Thread(target=even_num, args=(data,))
        t1.start()
