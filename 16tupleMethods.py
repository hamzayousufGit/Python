#There is not a way to change tuples but we can make a tuple a list then apply multitple operations and then we can convert it to a tuple

moreNumbers = [55, 12, 222]
newNumbers = (1, 2, 5, 99, 22, 67, 7, 0, 100)

newNumbers = list(newNumbers)

newNumbers.pop()
print(newNumbers)

newNumbers.sort()
print(newNumbers)

newNumbers.extend(moreNumbers)
print(newNumbers)

print(type(newNumbers))


newNumbers = tuple(newNumbers)
print(type(newNumbers), newNumbers)