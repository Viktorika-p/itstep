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
res = [ele for ele in d if ele != []]
print(res)


#варіант 2

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
res = list(filter(None, d))
print(res)
