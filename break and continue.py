i = 0
while (True):
    if i > 5:
        i = i + 1
        continue
    print(i + 1, end=" ")
    i = i + 1
    if i == 25:
        break