#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.
log = False
for c in range(1,1000):
    for b in range(1,c):
        for a in range(1,b):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a,b,c)
                log = True
        if log:
            break
    if log:
        break
