import json
from threading import Thread
import queue

def numbers(num):
    with open('test.json', 'r') as f:
    t = json.load(f)
    print(t)

def divide(data):
    positive = []
    negative = []
    for i in array:
        if i > 0:
            positive.append(i)
        else:
            negative.append(i)
    return positive, negative



arr_odd = [j for j in main_arr if j < 0]
arr_even = [j for j in main_arr if j >= 0]

print(f'Не чётный:{arr_odd}\nЧётный:{arr_even}')

if __name__ == "__main__":
    q = queue.Queue()
    t1 = Thread(target=lambda q, arg: q.put(divide(arg)), args=(q,))
    t1.start()
    t1.join()
    print(q.get())
