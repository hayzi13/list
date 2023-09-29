import random
a = int(input("введите число "))
q = [random.randint(0, 123)
for __ in range(10)]
print(q)
if a in q:
    print(q.index(a))
else:
    print('-1')
