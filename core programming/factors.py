num = int(input("Enter the value of the number:"))
sum = 0
for i in range(1,num+1):
    if(num%i == 0):
        print(i)
        sum = sum + 1

print("The sum of the factors is:", sum)        


            
    
