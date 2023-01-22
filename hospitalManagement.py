patient_list = []
condition_ = False
while(condition_ == False):
    print("1. View Pateints under Dr. Parth's care\n2.Add Patient\n3.Remove Patients\n4.Exit ")
    user_input = int(input("Enter your choice:"))
    if(user_input==4):
        condition_= True
    if(user_input==3):
        Removed_Patient = input("Enter patient Name to remove:")
        patient_list.remove(Removed_Patient)
        print(patient_list)
    if(user_input==2):
        Detail_List = []
        Name_input = input("Enter Full Name:")
        patient_list.append(Name_input)
        Age_input = input("Enter Age:")
        Contact_input = input("Enter Contact Number:")
        Address_input = input("Enter your Area:")
        dict_ = {'Name:':Name_input,'Age:':Age_input,'Contact info:':Contact_input,'Address:':Address_input}
        Detail_List.append(dict_)
    if(user_input==1):
        print(patient_list)
        user_input2 = input("Enter number to view Patient details:")
        print(Detail_List)
