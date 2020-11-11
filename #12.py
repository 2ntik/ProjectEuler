#Каково первое треугольное число, у которого более пятисот делителей?
from math import floor
from math import sqrt

tri_num = 3                                 # my triangular number
div = 2                                     # the number of dividers of the current triangular number
last_num = 2                                # last number i added to my triangular number

def is_sq(n):                               # if my number has sqrt, than there is 1 less devider
    x = floor(sqrt(n))
    if x**2 == n:
        return True
    else:
        return False

while div <= 500:
    div = 2
    last_num += 1
    tri_num += last_num
    for i in range(2, floor(sqrt(tri_num))):
        if tri_num % i == 0:
            div += 2
if is_sq(tri_num):
    div -= 1
print(tri_num)
