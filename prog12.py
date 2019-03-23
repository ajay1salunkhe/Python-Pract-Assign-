''' WAP tha accepts a sentence and calculate the number of  letters and digits. '''

class LettersDigits:
    strng = ""
    def getString(self):
        self.strng = input("Enter sentence : ")

    def showResult(self):
        digits,letters,other = 0,0,0
        for c in self.strng:
            if c.isdigit():
                digits += 1
            elif c.isalpha():
                letters += 1
            else:
                other += 1

        print("Total letters in string : ",letters)
        print("Total digits in string : ",digits)
        print("Other characters in string : ",other)

ld = LettersDigits()
ld.getString()
ld.showResult()



    