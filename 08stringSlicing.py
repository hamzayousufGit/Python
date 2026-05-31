#String Slicing means to slice a certain part of a string, it works with index for example
#Python
#012345  P = 0 y = 1 t = 2 h = 3 o = 4 n = 5, index of y is 1, note: index starts with 0
#but length of Python is 6

name = "HamzaPython"#length = 11

firstPart = name[0:5] #it means that start with index 0(H) and end with 5(P), we did 5 because it excludes the ending point/number/letter
print(firstPart)

lastPart = name[5]#it knows that I have to go till the last point 
print(lastPart)

randomSlicing = name[0:-1]#it means start with 0 and minus 1 from length of the variable( [0:lengthOfVariable-1] = [0:11-1] = [0:10] )

print(randomSlicing)