# Program to demonstrate list and tuple in python

#list
l1 = ["c","cpp","java","python"] #creating list

#changing list element
l1[0] = "assembly"

#iterating over list with index of list element
for i in l1:
    print(i)

print("Length of list : ",len(l1))

#list methods
l1.append("ruby") #appends an element to the end of the list
print(l1)

l2 = l1.copy() #returns a copy of the specified list

print("l1.count(\"python\") : ",l1.count("python")) #returns the number of elements with the specified value

l1.insert(0,"ada") #inserts the specified value at the specified position
print(l1)

l1.pop(0) #removes the element at the specified position
print(l1)

l1.reverse() #reverses the order of the list
print(l1)

l1.sort() #in ascending
print(l1) 
l1.sort(reverse=True) #in descending
print(l1)

l1.clear() #removes all the elements from a list
print("list after l1.clear() : ",l1)