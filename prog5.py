'''Write a program in Python, A library charges a fine for every book returned late.
For first 5 days the fine is 50 paisa, for 6-10 days fine is one rupee 
and above 10 days fine is 5 rupees. if you return the book after 30 days 
your membership will be cancelled. 
Write a program to accept the number of days the member is late to return the book 
and display the fine or the appropriate message '''

days = int(input("Enter no of late days : "))
if days>0:
    if days<=5:
        print("Fine is Rs.",days*0.5," (50 paisa per day)")
    elif days>5 and days<=10:
        print("Fine is Rs.",days*1," (1 Rs per day)")
    elif days>10 and days<=30:
        print("Fine is Rs.",days*5," (5 Rs per day)")
    elif days>30:
        print("Your membership cancelled")
else:
    print("days should be positive")