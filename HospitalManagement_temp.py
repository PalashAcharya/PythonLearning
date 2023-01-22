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
        Name_input = input("Enter Full Name of the Patient:")
        patient_list.append(Name_input)
    if(user_input==1):
        print(patient_list)
