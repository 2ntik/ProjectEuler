#Найдите сумму всех простых чисел меньше двух миллионов.

s = 0
lst = [2,3]         #list простых чисел
i = 3

while lst[-1] < 2000000:
    i += 2
    if i > 10 and i % 10 == 5:
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            s += i
            print(i)
            break
        if i % j == 0:
            break
    else:
        lst.append(i)
        print(i)
        s += i
print(s - lst[-1])
