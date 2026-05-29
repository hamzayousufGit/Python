#Type Casting, it means to change a datype of any value, like "1"(a string), type cast and boom 1(int)

name = input("What is your name?: ")#we need a string
print(name, type(name))#output: string, yes

age = input("What is your age?: ")
print(age, type(age))#output: string, no, we need a integer

age = int(age)
print(age, type(age))#output: integer, yes

num = "1n"#it can't do this, it says, what you wanna do bro? and throws an error
num = int(num)

print(num, type(num))