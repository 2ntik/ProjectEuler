#Каков самый большой делитель числа 600851475143, являющийся простым числом?

ish = 600851475143
ish2 = ish // 2
s = 0
lst = [2]         #list простых чисел

for i in range(3, ish2, 2):       #ищем все простые числа, на которые можно делить наше число
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
