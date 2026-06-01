#Break And Continue, Break: Exit the loop at a certain iteration Continue: Skips a certain iteration

#Continue
for i in range(21):
    if(i == 13):
        continue
    else:
        print(i)
        print("Lucky Number")

print("Loop 1 finished")

#Break
for j in range(21):
    if(j == 15):
        break
    else:
        print(j)

print("Loop 2 finished")