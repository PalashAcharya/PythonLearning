c = int(input("Enter the value: "))

d = c//2000
e = c%2000
f = e//500
e %= 500
a = e//200
e %= 200
h = e//100
e %= 100
j = e//50
e %= 50
l = e//20
e %= 20
n = e//10
e %= 10
p = e//5
e %= 5
r = e//2
e %= 2
t = e//1

print("Number of 2000 rs notes are:", d)
print("Number of 500 rs notes are:", f)
print("Number of 200 rs notes are:", a)
print("Number of 100 rs notes are:", h)
print("Number of 50 rs notes are:", j)
print("Number of 20 rs notes are: ", l)
print("Number of 10 rs notes are:", n)
print("Number of 5 rs coins are:", p)
print("Number of 2 rs coins are:", r)
print("Number of 1 rs coins are:", t)