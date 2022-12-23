def prime_num(num):
    sum = 0
    for i in range(1,num+1):
        if(num%i==0):
            sum = sum + 1
    if(sum==2):
        return "it is a prime number"
    else:
        return "it is not a prime number"    

num1 = int(input("Please enter the number:"))
print(prime_num(num1))
