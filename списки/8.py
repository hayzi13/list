a = int(input('введите число '))  
q = []
for i in range(a):
    w = int(input('введите число: '))
    q.append(w)
del q[1::2]
print(q)
