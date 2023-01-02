from user_defined_func_NumberOfDigits import Number_Of_Digits

def isarmstrong(num):
    range_ = Number_Of_Digits(num)
    remaining_num = num
    sum = 0
    while(remaining_num!=0):
        last_digit = remaining_num%10
        remaining_num = remaining_num//10
        new_num = last_digit*last_digit
        for i in range(1,range_-1):
            new_num = new_num*last_digit
        sum = sum + new_num
    if(sum==num):
        return True
    else:
        return False

num = isarmstrong(153)
print(num)
