f = open('myfirstfile.txt', 'a+')
input_str = input("Enter text:")
f.write(input_str)
f.close()

f = open('myfirstfile.txt', 'r')
input_str = f.read()
print(input_str)
f.close()
#w - for writing the data previously stored data is overwritten
#r - for reading the data and pointer is at the start of the file 
#a - to append a string at the end of the file previously stored data is not affected in this mode, pointer placed at the end
#w+ - writes and reads the data previously stored data is overwritten 
#r+ - reads and writes the data previously stored data will not be deleted, pointer is at the start of the file 
#a+ - appends and reads the data, previously stored data will not be deleted and pointer is at the end 

