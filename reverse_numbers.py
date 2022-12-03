num = int(input("Enter the number:"))
remaining_num = num 
reverse_num = 0
while(remaining_num!=0):
    last_digit = remaining_num%10
    reverse_num = reverse_num*10 + last_digit
    remaining_num = remaining_num//10

print("the reverse of the number is", reverse_num)






   