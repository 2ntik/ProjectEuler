'''
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
1 = one     11 = eleven     10 = ten        100 = one hundred  and ...    1000 = one thousand
2 = two     12 = twelve     20 = twenty     200 = two hundreds and ...
3 = three   13 = thirteen   30 = thirty     ...
4 = four    14 = fourteen   40 = forty
5 = five    15 = fifteen    50 = fifty
6 = six     16 = sixteen    60 = sixty
7 = seven   17 = seventeen  70 = seventy
8 = eight   18 = eighteen   80 = eighty
9 = nine    19 = nineteen   90 = ninety
'''

num = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
            18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30:'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
            80: 'eighty', 90:'ninety', 100: 'hundred'}

numbers = ''

for x in range(1,1001):
    if x == 1000:
        numbers += 'onethousand'
    else:
        if x > 99:
            z = x // 100
            x %= 100
            numbers += num[z] + num[100]
            if x != 0:
                numbers += 'and'
        if 9 < x < 20:
            numbers += num[x]
        else:
            y = x // 10 * 10
            x %= 10
            numbers += num[y]
            numbers += num[x]
print(numbers)
print(len(numbers))
