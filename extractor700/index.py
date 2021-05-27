userInput = input()

def desitky(numbers): # převede čísla např. 8, 4, 3 na 843
    x = 0
    i = 1
    for num in numbers:
        z = num * (10 ** (len(numbers) - i))
        x += z
        i += 1
    return x

numbers = []

i = 0
while i < len(userInput):  # projít písmeno po písmenu
    if (userInput[i].isdigit()):   # pokud je znak číslo
        num = []
        while userInput[i].isdigit(): # dokud je stále znak s pořadím i od začátku číslo
            num.append(ord(userInput[i]) - 48) # zkonvertovat ze znaku na číselnou hodnotu
            i += 1
            if(i >= len(userInput)): break;  # aby nespadl program, když je poslední znak číslo
        numbers.append(desitky(num))
    
    else: i += 1


print(sum(numbers))