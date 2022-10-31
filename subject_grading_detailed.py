marks_obtained = int(input("Enter your marks: "))

if(0<marks_obtained<=100):
    # print("We will be getting your grade shortly!")
    if(100 >=marks_obtained>=85):
        if(100 >= marks_obtained>=95):
            print("You got an A1")
        elif(marks_obtained>=90):
            print("You got an A2")
        else:
            print("You got A3")        
    elif(marks_obtained>=75):
        if(85>=marks_obtained>=80):
            print("You got B1")
        else:
            print("you got B2")    
        
    elif(marks_obtained>=65):
        if(75>=marks_obtained>=70):
            print("You got C1")
        else:
            print("You got a C2")
    elif(marks_obtained>=35):
        if(65>=marks_obtained>=55):
            print("You got a D1")
        elif(marks_obtained>=45):
            print("You got a D2")
        else:
            print("You got a D3")        
    else:
        print("You got an F")
else:
    print("Enter a valid number") 

