#Recursion, Recursion is when a function calls itself until a condition tells it to stop.
#We are going to use factorial(a maths lesson) of a number to understant this python topic.

#Factorial of 4: 4*3*2*1
#Factorial of 10: 10*9*8*7*6*5*4*3*2*1
#Factorial of 1: 1

def factorialNum(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorialNum(n - 1)
    
print(factorialNum(4))