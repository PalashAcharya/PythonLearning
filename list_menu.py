list_ = []
condition_ = True
while(condition_!=False):
    print("Menu:-\n1.Add a student name\n2.List of Students\n3.Search for student name\n4. Remove Student name\n5.Exit")
    user_input_ = int(input("Enter your choice:"))
    if(user_input_==1):
        name_input = str(input("Please enter a name: "))
        list_.append(name_input)
        print(list_)
    elif(user_input_==2):
        print(list_)
    elif(user_input_==4):
        unwanted_name = str(input("Enter the name to remove:"))
        list_.remove(unwanted_name)
        print(list_)
    elif(user_input_==3):                                                 #can also use list_.count as if(list_.count !=0): name is present else it is not 
        search_name = str(input("Enter the name to search for student:"))
        length_= len(list_)
        for i in range(1,length_+1):
            if(search_name==list_[i-1]):
                print("Name is present")
                break
            else:
                if(i==length_ and search_name!=list_[i-1]):
                    print("Name is not present")
    else:
        condition_= False

    