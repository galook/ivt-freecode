import math
worthless = input()
worthless = None
numbersOne = input().split(' ')
numbersTwo = input().split(' ')
rNumbers = []
def concat(): 
    i = 0
    while (i < len(numbersOne)):
        rNumbers.append(int(numbersOne[i]))
        i += 1
    i = 0
    while (i < len(numbersTwo)):
        rNumbers.append(int(numbersTwo[i]))
        i += 1
concat()

res = [math.inf]
def sort(): 
    i = 0

    while (i < len(rNumbers)):
        p = 0
        while (p < len(rNumbers)):
            if(rNumbers[i] < res[p]):
                res.insert(p, rNumbers[i])
                break  
            p += 1  
        i += 1

sort()

i = 0
while i < len(res):
    res[i] = str(res[i])
    i += 1

res.pop()
separ = ', '
print(separ.join(res))


