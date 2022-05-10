oli = ["[","{","("]
clit = ["]","}",")"]

def isCorrect(inp):
    parenthes = []
    for i in inp:
        if i in oli: parenthes.append(i)
        elif i in clit:
            pos = clit.index(i)
            if ((len(parenthes) > 0) & (oli[pos] == parenthes[len(parenthes)-1])): parenthes.pop()
            else: return "FAIL"
    if len(parenthes) == 0: return "OK"
    else: return "FAIL"


inp = input()
print(isCorrect(inp))
    
