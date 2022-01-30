list = {(0, 0), (1, 1), (2, 2), (3, 3)}

i, j = (0, 0)
while (i, j) in list:
    i += 1
    j += 1
    print(i, j)
print(i, j)
