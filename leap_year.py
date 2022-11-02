y = int(input("Enter the year:"))

if(y%4==0):
    if(y%100==0 and y%400==0):
        print("It is a leap year")
    elif(y%100==0 and y%400!=0):
        print("It is not a leap year")
    elif(y%100!=0 and y%400!=0):
        print("It is a leap year")
else:
    print("It is not a leap year")            

