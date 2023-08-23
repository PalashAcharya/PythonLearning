def artithmetic_arranger(List,bool):
    length_ = len(List)
    if length_ >5:
        raise ValueError("There must only be 5 operations")
    tuple_list = []
    result_list=[]
    for elements in List:
        if "+" in elements:
            tuple_list.append(list(elements.partition("+")))
        elif "-" in elements:
            tuple_list.append(list(elements.partition("-")))
        elif "*" in elements:
            raise ValueError("Operator must be '+' or '-'")
        elif "/" in elements:
            raise ValueError("Operator must be '+' or '-'")
    for i in range(length_):
        for j in range(3):
            if j==1:
                pass
            else:
                str(tuple_list[i][j])
                tuple_list[i][j]=tuple_list[i][j].rjust(4)
    if(bool==True):
        for var in tuple_list:
            if(var[1]=="+"):
                try:
                    op1 = int(var[0])
                    op2 = int(var[2])
                    res = op1+op2
                    result_list.append(str(res))
                except:
                    raise ValueError("Operands can only be digits")
            else:
                try:
                    op1 = int(var[0])
                    op2 = int(var[2])
                    res=op1-op2
                    result_list.append(str(res))
                except:
                    raise ValueError("Operands can only be digits")
        adj_result_str=result_list[0].rjust(5)
        result_String = adj_result_str
        for var in range(1,length_):
            adj_result_str = result_list[var].rjust(5)
            result_String = result_String+"    "+adj_result_str
        format_string = Format(tuple_list,length_)+"\n"+result_String
        return format_string
    else:
        format_string = Format(tuple_list,length_)
        return format_string

def Format(element_list,length):
    if(length>0):
        format_string1 = " "+element_list[0][0]
        format_string2 = element_list[0][1]+element_list[0][2]
        format_string3 = "-----"
        for i in range(1,length):
            format_string1 = format_string1 + "     "+element_list[i][0]
            format_string2 = format_string2 + "    "+element_list[i][1]+element_list[i][2]
            format_string3 = format_string3 + "    "+"-----"
        final_string = format_string1 + "\n" + format_string2+"\n"+format_string3
        return final_string
    else:
        return -1

L1 = ["1234+4231","1234+2421","1234+3321","1123+1234","9999+9999"]
print(artithmetic_arranger(L1,True))