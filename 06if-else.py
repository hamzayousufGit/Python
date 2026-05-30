#IF-ELSE CONDITIONS

#Syntax
#if(condition == true):
#   do this
#else:
    # do this    

# EXAMPLE 1
age = 10

if(age >= 18):
    print("You CAN drive")
else:
    print("You CANNOT drive")
    
# EXAMPLE 2
isStudent = True

if(isStudent == True):
    print("You CAN enter in the school")
else:
    print("You CANNOT enter the school")
    
# ELIF CONDITIONS
#in elif we can give more conditions with elif

#EXAMPLE
userAge = int(input("Enter your age: "))

if(userAge < 0):
    print("Your age cannot be below 0")
elif(userAge > 100):
    print("Your age cannot be greater than 100")
elif(userAge == 0):
    print("Congrats, you are just born")
elif(userAge <= 10):
    print("You are a kid")
elif(userAge > 10 and userAge <= 17):
    print("You are a boy")
elif(userAge > 17 and userAge <= 50):
    print("You are an adult")
else:
    print("You are an old person")