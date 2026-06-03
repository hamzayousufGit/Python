#List Methods, by list methods we can do various operations with a list

numbers = [3, 1, 2, 5, 4, 7, 6]

#append, add a element to the end of a list
append = numbers.append(8)
print(numbers)

#sort, align items in a order present in a list
sort = numbers.sort()
print(numbers)
sortReverse = numbers.sort(reverse = True)
print(numbers)

#pop, deletes a element by giving the index of that element
pop = numbers.pop(3)
print(pop)
print(numbers)

#index, this method returns a index of the element which we give to it
index = numbers.index(8)
print(index)

#insert, this methods inserts a element at a specific index
insert = numbers.insert(3, 123)
print(numbers)

#copy, it copies a list
copy = numbers.copy()
copy[0] = 67
print(numbers)
print(copy)

#extend, puts elements of a list into the end of another list
fakeNumbers = ["2", "67", "8", "6"]
extend = numbers.extend(fakeNumbers)
print(numbers)
