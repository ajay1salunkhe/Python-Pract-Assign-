''' Write a function that recieves marks received by a student in 3 subjects and returns the average 
and percentage of these marks. call this function from main() and print the result in main. '''

def calculateAvgPerc():
    total = []
    noStud = int(input("Enter no of students : "))
    for i in range(noStud):
        sum = 0
        print("-------------------------------")
        print("Enter details for student "+str(i+1))
        for j in range(3):
            sum += int(input("Enter marks of subject "+str(j+1)+" : "))
        total.append(sum)
    
    for i in range(noStud):
        print("-------------------------------")
        print("Result of Student ",i+1," : ")
        print("Total : ",total[i])
        print("Percentage : ","{0:.2f}".format((total[i]/300)*100))

    



def main():
    calculateAvgPerc()

if __name__=="__main__":
    main()

