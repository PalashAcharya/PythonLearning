x = int(input("Enter the number:"))
number_of_digits = 0
remaining_number = x
while(remaining_number != 0):
    remaining_number = remaining_number//10
    number_of_digits = number_of_digits + 1

print("The number of digits are:", number_of_digits)