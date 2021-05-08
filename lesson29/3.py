from threading import Thread
import queue

class Search_key:
    def search_keywords(key):
        results = set()

        with open('test1.txt') as f:
            for line in f:
                words = line.strip().lower()
                kws_present = True
                for i in key:
                    kws_present = i in words
                if not kws_present:
                    break
                if kws_present:
                    results.add(line)
        return sorted(list(results))

        with open('test2.txt') as d:
            for line in d:
                list = line.strip().lower()
                kws_present = True
                for d in keywords:
                    d = keyword in list
                    if not kws_present:
                        break
                if kws_present:
                    results.add(line)
        return sorted(list(results))

if __name__ == "__main__":
    q = queue.Queue()
    t1 = Thread(target=search_keywords, args=(q,))
    t1.start()
    t1.join()
    print(q.get())
