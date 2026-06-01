#Functions, a way to reuse a code that needs to be repeat many times in future, also use to write less code, To print a function we have to call it


#Add Two Numbers
def addTwoNumbers(a, b):
    logicA = a + b
    print(logicA)

firstNumberA = int(input("Enter your first number to add: "))
secondNumberA = int(input("Enter your second number to add: "))
addTwoNumbers(firstNumberA, secondNumberA)


#Multiply Two Numbers
def multiplyTwoNumbers(c, d):
    logicM = c * d
    print(logicM)

firstNumberM = int(input("Enter your first number to multiply: "))
secondNumberM = int(input("Enter your second number to multiply: "))
multiplyTwoNumbers(firstNumberM, secondNumberM)


#Subtract Two Numbers
def subtractTwoNumbers(e, f):
    logicS = e * f
    print(logicS)

firstNumberS = int(input("Enter your first number to subtract: "))
secondNumberS = int(input("Enter your second number to subtract: "))
subtractTwoNumbers(firstNumberS, secondNumberS)

#Divide Two Numbers
def divideTwoNumbers(e, f):
    logicD = e * f
    print(logicD)

firstNumberD = int(input("Enter your first number to divide: "))
secondNumberD = int(input("Enter your second number to divide: "))
divideTwoNumbers(firstNumberD, secondNumberD)