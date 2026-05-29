#Inputs

#                           EXAMPLE
#name = input("What is your name?: ") #output datatype: STRING
#print(type(name))

name = input("what is your name?: ")
favFood = input("What is you favourite food?: ")
age = input("What is your age?: ")

result = f"""Your name is {name}\nYou are {age} years old\nYour favourite food is {favFood}     \nBye Bye"""#these are f strings, these help you to use variables in a string
print(result)