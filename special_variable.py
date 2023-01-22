def display():
    print("Hello world!")
print(__name__)
if __name__ == '__main__':
    display()
    print("This code is run without importing a module")
else:
    print("This code is run with importing a module")