import random
a = []
for i in range(10):
    a.append(random.randint(0, 25))
q = a.copy()
maximum = a.index(max(a))
minimum = a.index(min(a))
a[maximum] = min(a)
a[minimum] = max(a)
print(a)
print(q)
