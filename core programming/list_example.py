a = [1,30,45,45]
#print(a[2])
#print(len(a))
#print(type(a))
a.append(11)
print(a)
a.insert(1,40)
#a.clear()
#print(a[1:3])
a.remove(30)
for i in a: 
    print(i)


a.extend([124,48])
#print(a)
#it can also be used for extending the list with another list 
#print(a.pop())
#print(a.index(1))
print(a.count(29))
a.sort()
a.reverse()
a2 = a.copy()
a_max = max(a)
#print(a_max)
#print(a)
a[0]= 20
#print(a)
