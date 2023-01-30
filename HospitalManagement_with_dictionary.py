patient_dict = {}
patient_detail_dict = {}
condition_ = False
patient_num = 0
while(condition_== False):
    print("1. Add a Patient\n2. View patient detials\n3. search for patient\n4. exit ")
    user_input = input("Enter your choice:")
    try:
        user_input = int(user_input)
    except:
        print("Not a number")
    if(user_input==1):
        patient_num = patient_num +1 
        str_patient_num = str(patient_num)
        Name_input = input("Enter Patient's name:")
        Age_input = input("Enter patient's Age:")
        address_input = input("Enter Patient's address:")
        patient_detail_dict = {'Name': Name_input,'age': Age_input, 'Address': address_input}
        patient_dict[str_patient_num] = patient_detail_dict
        print(list(patient_dict))
    elif(user_input==2):
        for x in patient_dict:
            print(x)
        user_input2 = input("Enter the patient number to view their details:")
        details_ = patient_dict[user_input2]
        print(details_)
        #for k, v in patient_dict.items():
            #if(user_input2==k):
                #print(v)
    elif(user_input==3):
        search_number = input("Enter the Patient number to find:")
        search_factor = search_number in patient_dict
        if(search_factor==True):
            print("Patient is present")
            answer = patient_dict[search_number]
            print(answer)
        else:
            print("Patient is not present")
    else:
        condition_ = True        