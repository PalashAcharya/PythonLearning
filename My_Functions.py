def Number_Of_Digits(num):
    digits_ = 0
    while(num!=0):
        num = num//10
        digits_ = digits_ + 1
    return digits_  

def Sum_Of_Digits(num):
    sum = 0
    while(num!=0):
        last_digit = num%10
        num = num//10
        sum = sum + last_digit
    return sum

def Reverse_num(num):
    reverse_num = 0
    while(num!=0):
        last_digit = num%10
        num = num//10
        reverse_num = reverse_num*10 + last_digit
    return reverse_num

def Is_Palindrome_Num(num):
    reverse_num = Reverse_num(num)
    if(num == reverse_num):
        return True
    else:
        return False 