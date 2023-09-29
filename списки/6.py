import random
a = []
for i in range(10):
    a.append(random.randint(0, 10))
print(a)
for q in a:
    if a.count(q) > 1:
        print(q)
