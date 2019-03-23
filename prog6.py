'''Write a program to calculate overtime pay of 10 employees. 
Overtime is paid at the rate of Rs.12.00 per hour for every hour worked above 40 hours. 
Assume that employee do not work for fractional part of an hour. '''

emps = int(input("Enter no of employees : "))

for i in range(emps):
    print("\n For employee no ",i+1)
    hrs = int(input("Enter work in hrs : "))
    if hrs>0:
        if hrs>40:
            print("Overtime pay is Rs.",12*(hrs-40)," (Rs. 12 per hr)")
        else:
            print("Overtime pay is applicable over 40 hr. only")
    else:
        print("Hrs should be positive")
        exit()