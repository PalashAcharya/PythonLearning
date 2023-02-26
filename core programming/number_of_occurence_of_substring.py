string_ = input("Enter the String:")
substring_ = input("Enter the substring:")
count = 0
find_ = string_.find(substring_)
if(find_==-1):
    print("The Substring is not present")
while(find_!=-1):
    count = count + 1
    find_ = find_+1
    find_ = string_.find(substring_,find_)
print("The number of times it occurs is:",count)





