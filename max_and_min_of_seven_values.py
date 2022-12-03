for i in range(1,8):
    x = int(input("Enter values:"))
    if(i==1):
        max = x
        min = x
    if(x>max):
        max = x
    if(x<min):
        min = x    
    


print("The maximum value is", max)
print("The minimum value is:", min)

