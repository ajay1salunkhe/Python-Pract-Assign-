''' Define a class with two methods: 
    getString() : to get string from console input
    putString() : to print string in upper case
    class methods of class by creating object.
'''

class UpperString:
    strng = ""
    def getString(self):
        self.strng = input("Enter string : ")

    def putString(self):
        print("String in Uppercase : ",self.strng.upper())

obj = UpperString() #creating object
obj.getString() # calling method with object
obj.putString()
