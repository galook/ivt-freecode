cisloKHovnu = input()
string = input()
move = True
while move:
    try: 
        index = string.index('?')
        before = string[index - 1]
        after = string[index + 1]
    except ValueError:
        move = False
        break
    except IndexError:
        beforeLarge = (ord(before) >= 65 and ord(before) <= 90)
        beforeSmall = (ord(before) >= 97 and ord(before) <= 122)
        if beforeLarge: string = string[:index] + 'a'
        if beforeSmall: string = string[:index] + 'A'
        break



   
    beforeLarge = (ord(before) >= 65 and ord(before) <= 90)
    afterLarge = (ord(after) >= 65 and ord(after) <= 90)
    beforeSmall = (ord(before) >= 97 and ord(before) <= 122)
    afterSmall = (ord(after) >= 97 and ord(after) <= 122)

    if (beforeLarge and afterLarge):
        string = string[:index] + 'a' + string[index + 1:]
    if ((beforeSmall and afterSmall)):
        string = string[:index] + 'A' + string[index + 1:]
    if ((beforeLarge and afterSmall) or (beforeSmall and afterLarge)):
        string = "-1"


print(string)


