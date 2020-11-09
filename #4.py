#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
flag = False
ans = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        ch = str(i*j)
        if ch == ch[::-1]:
            if int(ch) > ans:
                ans = int(ch)
print(ans)
