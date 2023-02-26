a = int(input("Enter your marks in science subject:"))

b = int(input("Enter your marks in math subject:"))
if((a>=0 and a<=100) and (b>=0 and b<=100)):    
    if(a>=40 and b>=40):
        print("You passed!")
    
    else:
        print("You failed")        
else:
    print("Please enter a valid number")                              