'''
A cahier has currency notes of denominations 10,50 and 100.
If the amount to be withdrawn is input through the keyboard using input() function in hundreds,
find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
'''

amount = int(input("Enter amount : "))

if amount%100 == 0:
    print("Cashier have to give ",int(amount/10)," notes of Rs. 10 \n or")
    print("Cashier have to give ",int(amount/50)," notes of Rs. 50 \n or")
    print("Cashier have to give ",int(amount/100)," notes of Rs. 100")
else:
    print("Please enter amount in multiple of hundreds.")

