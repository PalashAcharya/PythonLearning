import random
string_ = "appreciation"
condition_ = False
length_ = len(string_)
n = length_//2
random_num_set = set()
while(condition_== False):
    for k in range(0,n+1):
        random_num = random.randint(0,length_-1)
        random_num_set.add(random_num)  
    if(len(random_num_set)==n):
        condition_= True
    else:
        continue
string_list= list(string_)
for i in random_num_set:
    string_list[i]= "_"
newstring_ = ""
for j in string_list:
    newstring_ = newstring_ + j
print(newstring_)
for z in range(0,length_+1):
    print(z,end =",")
condition2 = False
while(condition2==False):
    user_string = ""
    for x in random_num_set:
        print("\nEnter",x,"th Letter:")
        user_input = input()
        string_list[x] = user_input
    for y in string_list:
        user_string = user_string + y
    if(user_string==string_):
        print("It's a match!")
        condition2= True
    else:
        print("Try again")