def Factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

num = int(input("Enter The Number:"))
fact = Factorial(num)
print("Factorial of the number is:",fact)