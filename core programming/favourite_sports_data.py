count = 0
list_ = []
while(count<5):
    user_input = int(input("Enter your roll Number:"))
    user_input2 = str(input("Enter your favourite sport:"))
    #dict_ = {'Roll Number':user_input,'Favourite Sport':user_input2}
    dict_ = {}
    dict_[user_input]= user_input2
    list_.append(dict_)
    count = count + 1
    for k,v in dict_.items():
        print(k,v)
print(list_)
