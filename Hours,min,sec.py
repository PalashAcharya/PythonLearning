i = int(input("Enter time in sec: "))

h = i//3600
m = i%3600
mf = m//60
s =  m%60

print( h, "hours")
print(mf, "min")
print(s, "Seconds")
