for i in range(2,21):
    n = i
    sum=0
    for j in range(1,n+1):
        if(n%j==0):
            sum= sum + 1
    if(sum==2):
        print(n)       



