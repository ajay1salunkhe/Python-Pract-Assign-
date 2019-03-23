''' Write  to program to read a file and display its content '''

filename = input("Enter file name to read its content (with extension) : ")

f = open(filename,"r")
print("---------------------------------------------")
print("File Content of ",filename)
print("---------------------------------------------")
print(f.read())
print("---------------------------------------------")