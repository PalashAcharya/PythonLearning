num = int(input("Enter the value of number:"))
sum = 0
for i in range(1, num+1):
    if(num%i==0):
        sum = sum +1

if(sum==2):
    print("It is a prime number")
else:
    print("It is not a prime number")    