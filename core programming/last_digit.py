x = int(input("Enter the number:"))

last_digit = x%10
#remaining_numbers = x - last_digit
remaining_numbers = x//10

print("The last digit of the number is:", last_digit)
print("The remaining numbers are:", remaining_numbers)      