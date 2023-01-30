patient_list = []
Detail_list = []
condition_ = False
while(condition_==False):
    print("1. Add a patient\n2. View Patient details\n3. Search for patient\n4. Exit")
    try:
        user_input = int(input("Enter your choice:"))
    except:
        print("Not a Number")
    if(user_input==1):
        Name_input = input("Enter your full name:")
        patient_list.append(Name_input)
        Age_input = input("Enter your age:")
        Contact_input = input("Enter your contact number:")
        Address_input = input("Enter your address")
        Patient_dict = {'Name': Name_input, 'Age': Age_input, 'Contact': Contact_input, 'Address': Address_input}
        Detail_list.append(Patient_dict)
    elif(user_input==2):
        print(patient_list)
        print(Detail_list) 
    elif(user_input==3):
        search_name = input("Enter patient's name:")
        length_ = len(Detail_list)
        isavailable = False
        for patient_ in range(1,length_+1):
            x = Detail_list[patient_-1]
            if(search_name == x['Name']):
                print("Patient is present")
                print(x)
                isavailable = True
                break
        if(isavailable== False):
            print("Patient is not present")
    else:
        condition_= True
        