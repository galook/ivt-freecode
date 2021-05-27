input = input().split("_")
numbers = []
for word in input:
    if (word.isdigit()):
        length = len(word) - 1
        finalNumber = 0
        i = 0
        for char in word:
            finalNumber += ((ord(char) - 48) * (10 ** (length - i)))
            i += 1
        numbers.append(finalNumber)
print(sum(numbers))