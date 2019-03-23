# Program to demonstrate list and tuple in python

#tuple

t1 = ("c","cpp","java","python") #creating tuple

try:
    pass
    #t1[0] = "assembly" #tuple elements are immutable
except Exception as e:
    print(e)

#looping tuple
for t in t1:
    print(t)

print("Length of tuple : ",len(t1))

#tuple methods
print("t1.count(\"python\") : ",t1.count("python")) #returns the number of elements with the specified value

print(t1.index("cpp")) #finds the first occurrence of the specified value
try:
    print(t1.index("try")) #raises an exception if the value is not found
except Exception as e:
    print(e)
