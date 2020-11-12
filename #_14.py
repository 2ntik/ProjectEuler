#Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
#n → n/2 (n - четное)
#n → 3n + 1 (n - нечетное)

max = 0
max_num = 0

for i in range(1000000, 1, -1):
    num = i
    am = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            am += 1
        else:
            num = 3 * num + 1
            am += 1
    if am > max:
        max = am
        max_num = i
print(max, max_num)
