import re
import json


class Workers:

    def __init__(self, workers: list) -> None:
        self.__workers = workers

    def __iter__(self):
        return iter(self.__workers)

    def __getitem__(self, item):
        print("add_worker", item)
        return f"Worker {self.__workers[item]}"

    def __next__(self):
        pass

    def add_to_list(self, workers):
        with open('data.json', 'w') as f:
            json.dump(workers, f)

if __name__ == "__main__":
    list = Workers(['Test', 'Test2', 'Test3'])
    for i in list:
        print(i, end= " ")
    print("\n")
