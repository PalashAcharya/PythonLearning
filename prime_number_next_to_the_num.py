num = int(input("Enter the number:"))
n = num +1
sum_p = False
while(sum_p==False):
    sum = 0
    for i in range(1,n+1):
        if(n%i==0):
            sum = sum +1
    if(sum==2):
        print("The prime number after the inserted number is:",n)
        sum_p= True
    n = n+1    