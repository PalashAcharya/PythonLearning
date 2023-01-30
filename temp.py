data = {'name': 'palash', 'age':'18'}
data_list = {}
data_list['101']= data
data2 = {'name': 'varun', 'age': '19'}
data_list['102'] = data2
print(data_list)
for x in data_list:
    print(x)
    y = data_list[x]
    print(y)
searchfactor = '101' in data_list
print(searchfactor)