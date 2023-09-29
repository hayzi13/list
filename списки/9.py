a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
w = []
for i in a:
    if i in a and i in q:
        w.append(i)
print(w)
