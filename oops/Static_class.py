class MyMath:
    @staticmethod
    def Add(a,b):
        return a+b
    @staticmethod
    def factors(num):
        factrs = 0
        for i in range(1,num+1):
            if(num%i==0):
                factrs = factrs+1
        return factrs
    @staticmethod
    def isprime(num):
        factrs = MyMath.factors(num)
        if(factrs==2):
            return True
        else:
            return False
    
print(MyMath.Add(1,3))
print(MyMath.factors(10))
x = MyMath.isprime(7)
if(x==True):
    print("It is a prime number")
else:
    print("Its not a prime number")