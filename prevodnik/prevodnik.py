def baseCalculator(basero, numero): 
    if not numero:
        return "0"
    else:
        return baseCalculator(basero, numero//basero).lstrip("0") + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[numero%basero]

res = []

while True:
    base = int(input())
    if not base in range(2, 17):
         break
    number = int(input())
    res.append(str(baseCalculator(base, number)))
    
print('\n'.join(res))