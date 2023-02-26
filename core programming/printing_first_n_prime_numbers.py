num = int(input("Enter the desired number of prime numbers to print:"))
prime_series = 1
n = 2
while(prime_series<=num):
    sum = 0
    for i in range(1,n+1):
        if(n%i==0):
            sum = sum+1
    if(sum==2):
        prime_series = prime_series +1
        print(n)        
    n = n +1