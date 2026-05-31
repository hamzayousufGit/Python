# For Loops, to repeat something with certain times

#for i in range(10):
 #   print(i)#it will exclude the last number output: 1 2 3 4 5 6 7 8 9
    
#for i in range(10):
#     print(i + 1)
    
# for i in "Python":
#     print(i)
    
# for j in range(2, 22, 2):#start with 0 end with 22(20), jump two times in every iteration
#     print(j)

for i in ["RED", "GREEN", "ORANGE", "PURPLE"]:
    print(i)
    for j in i:
        print(j)