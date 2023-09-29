import random
a = []
for i in range(10):
    a.append(random.randint(0, 25))
print(a)
q = 0
w = 1
for i in a:
    q += i
    w *= i
print(q)
print(w)
