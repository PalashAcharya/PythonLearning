num = int(input("Enter the number:"))
sum = 0
remaining_num = num
while(remaining_num != 0):
    last_digit = remaining_num%10
    sum = sum + last_digit
    remaining_num = remaining_num//10
    

print("The sum of digits of the number", num, "is:", sum)    

