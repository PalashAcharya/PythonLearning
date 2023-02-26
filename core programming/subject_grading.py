marks_obtained = int(input("Enter your marks: "))

if(0<marks_obtained<=100):
    # print("We will be getting your grade shortly!")
    if(100 >=marks_obtained>=85):
        print("You got an A")
    elif(marks_obtained>=75):
        print("You got a B")
    elif(marks_obtained>=65):
        print("You got a C")
    elif(marks_obtained>=35):
        print("You got a D")
    else:
        print("You got an F")
else:
    print("Enter a valid number") 

