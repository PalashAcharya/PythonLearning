def add_time(start,duration,optional=None):
    period_list = ["AM","PM"]
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    start = start.split()
    opp_per = [i for i in period_list if i!=start[1]]
    time = start[0].split(":")
    start_hrs = int(time[0])
    start_min = int(time[1])
    duration = duration.split(":")
    dur_hrs = int(duration[0])
    dur_min = int(duration[1])
    total_min = start_hrs*60+dur_hrs*60+start_min+dur_min
    days_passed = total_min//1440
    res_hrs = total_min//60
    res_min = total_min%60
    if(res_min>60):
        res_hrs = res_hrs+res_min//60
        res_min = res_min%60
    per_flips = res_hrs//12
    if(per_flips%2==0):
        res_per = str(start[1])
    else:
        res_per = str(opp_per[0])
    if(start[1]=='PM' and res_per=='AM'):
      days_passed +=1
    if(res_hrs==12 and res_per=='AM'):
        res_time = str(res_hrs)+":"+str(res_min).zfill(2)+" "+ str(res_per)+" "+"(next day)"
    elif(res_hrs>12):
        res_hrs = res_hrs%12
        if(res_hrs==0):
            res_hrs=12
        if(days_passed==1):
            res_time = str(res_hrs)+":"+str(res_min).zfill(2)+" "+str(res_per)+" "+"(next day)"
        elif days_passed>1:
            res_time = str(res_hrs)+":"+str(res_min).zfill(2)+" "+str(res_per)+" "+ f"({days_passed} days later)"
        else:
            res_time = str(res_hrs)+":"+str(res_min).zfill(2)+" "+str(res_per)
    elif(res_hrs==12 and res_per=="PM"):
        res_time = str(res_hrs)+":"+str(res_min).zfill(2)+" "+str(res_per)
    else:
        res_time = str(res_hrs)+":"+str(res_min).zfill(2)+" "+str(res_per)
    if optional:
        start_day_index = days.index(optional.capitalize())
        end_day_index = (start_day_index+days_passed)%7
        end_day = days[end_day_index]
        if(days_passed==1):
            return f'{str(res_hrs)}:{str(res_min).zfill(2)} {str(res_per)}, {str(end_day)} (next day)'
        elif days_passed>1:
            return f'{str(res_hrs)}:{str(res_min).zfill(2)} {str(res_per)}, {str(end_day)} ({days_passed} days later)'
        else:
            return f'{str(res_hrs)}:{str(res_min).zfill(2)} {str(res_per)}, {str(end_day)}'
    return res_time

print(add_time("3:30 PM","2:12","Monday"))