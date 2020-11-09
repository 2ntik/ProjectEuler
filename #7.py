#Какое число является 10001-ым простым числом?

s = 0
lst = [2,3]         #list простых чисел
i = 3

while len(lst) < 10001:
    i += 2
    if len(lst) >= 10001:
        break
    if i > 10 and i % 10 == 5:
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            print(i)
            break
        if i % j == 0:
            break
    else:
        lst.append(i)
        print(i)
print(lst[-1])
