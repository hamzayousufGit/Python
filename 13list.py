#List, if you have to put multiple strings, number etc in one entity, you can use a list

fruits = ["apple", "cherry", "pineapple", "strawberry"] #again, its length is 4, but in index, it ends with 3, 0 = "apple", 1 = "cherry", 2 = "pineapple", 3 = "strawberry"

for fruit in fruits:
    print(fruit)

games = ["GTA5", "roblox", "temple run", "subway sufer"]

print(games)
print("the best game award goes to ", games[-3])#games[length(games) - 3] = games[4 - 3] = games[1]

colors = ["green", "red", "purple", "blue", "yellow"]
print(colors)

for color in colors:
    print(color)
    for char in color:
        print(char)


#exercise: make a quiz of science using if-else, inputs, variables and(optional) lists and loops