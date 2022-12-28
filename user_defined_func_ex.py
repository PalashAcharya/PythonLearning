def prime_num(num):
    sum = 0
    for i in range(1,num+1):
        if(num%i==0):
            sum = sum + 1
    if(sum==2):
        return True
    else:
        return False

num = int(input("Enter the number:"))
if(prime_num(num)==True):
    print("It is a prime number")
else:
    print("It is not a prime number")

def prime_num_first_five():
    count = 0
    n = 2
    while(count<5):
        sum = 0
        result = prime_num(n)
        if(result):
            count = count + 1
            print(n)
        n = n + 1
    #return True
         

prime_num_first_five()

def prime_num_next_to_num(num):
    num = num + 1
    condition_ = False
    while(condition_== False):
        is_prime = prime_num(num)
        if(is_prime):
            #condition_=True
            return num
        num = num + 1

print(prime_num_next_to_num(7))            
        
            




