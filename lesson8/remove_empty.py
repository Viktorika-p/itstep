a = []
for i in range(1, 10):
    a.append(i)
print(a)

b = [i for i in range(1,10)]
print(b)

c = [i*2 for i in range(1,10)]
print(c)

even = []
d = a + b + c
filter(lambda x: len(x) > 0, d)
print(d)
