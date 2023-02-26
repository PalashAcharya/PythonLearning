num = int(input("Enter the number:"))
reverse_num = 0
remaining_num = num
while(remaining_num !=0):
    last_digit = remaining_num%10
    reverse_num = reverse_num*10 + last_digit
    remaining_num = remaining_num//10

if(reverse_num==num):
    print("It is a Palindrom Number")
else:
    print("It is not a Palindrom Number")    
