i = int(input("Enter the value: "))

h = i//3600
m = i%3600
mf = m//60
s =  m%60

print("The value will be ", h, "hours")
print(mf, "min")
print(s, "Seconds")
