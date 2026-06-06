#Tuple, its a type of a list but can't change, its immutable

specialFruits = ("apple", "charry", "dragon fruit", "pineapple") 
print(type(specialFruits), specialFruits) 

numbers = (4) 
print(type(numbers), numbers)#python gets confuse and says its a integer, because there is only 1 number, to change this we have to add a coma after it 

newNumbers = (4,) 
print(type(newNumbers), newNumbers)