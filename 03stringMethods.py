name = "hamza yousuf!"
print(name)

upperName = name.upper()
print(upperName, "String methods always give a new string")

lowerName = name.lower()
print(lowerName, "String methods always give a new string")

firstNameBySlicing = name[0:5] #name[:5] is also same as this
print(firstNameBySlicing)

lastNameBySlicing = name[6:] #name[6:(to last)] is also same as this
print(lastNameBySlicing)

splitedName = name.split()
print(splitedName)

removeCharInName = name.rstrip("!")
print(removeCharInName)

titledName = name.title()
print(titledName)

capitalizedName = name.capitalize()
print(capitalizedName)

indexOfAnyCharInName = name.index("a")
print(indexOfAnyCharInName)