#Какова сумма цифр числа 2**1000?

sum = 0
num = 2**1000

while num != 0:
    sum += num % 10
    num //= 10

print(sum)