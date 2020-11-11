# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import time
start_time = time.time()
ish = 600851475143 // 2
s = 3
lst = []
marker = False
while s**2 <= ish:
    if ish % s == 0 and s not in lst:
        lst.append(s)
        lst.append(ish//s)
    s += 2
print("--- %s seconds ---" % (time.time() - start_time))
lst.sort()
for i in range(len(lst)+1, 0, -1):
    if i > 10 and i % 10 == 5:
        continue
    for j in lst:
        if j * j - 1 > i:
            s = i
            marker = True
            break
        if i % j == 0:
            break
    else:
        s = i
        marker = True
    if marker:
        break
print(lst[-1])
