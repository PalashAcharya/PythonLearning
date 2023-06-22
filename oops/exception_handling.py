x = input("Enter Number one:")
y = input("Enter Number two:")
try:                                                      
    x = int(x)
    y = int(y)
    print("Division is,",x/y)
except ZeroDivisionError:
    print("Zero was given as second argument")
except ValueError:
    print("Invalid data entered! Please enter an integer")
except:
    print("Something went wrong!")
finally:
    print("Program is executed!")