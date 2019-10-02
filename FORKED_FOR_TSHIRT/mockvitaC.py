str = str (input("Enter comma separated integers: "))
list = str.split (",")
li = []
count=0
date='1'
d=0
valid=0
date1=None
date2=None
month1=None
month2=None
time1=None
time2=None
time3=None
time4=None
for i in list:
	li.append(int(i))
	count=count+1
if count!=12:
    print('0')
else:
    
    for i in range(11):
        if li[i]>li[i+1]:
            print('0')
            valid=valid+1
        else:
            d=d
    if valid==0:
        if 1 and 0 in li:
                month1=1
                li.remove(1)
        elif 0 in li:
                month1=0
                li.remove(0)
        elif 1 in li:
                month1=1
        else:
                d=d
        for i in range(3):
            if i in li:
                month2=i
            else:
                d=d
    
    li.remove(month2)

    for i in range(4):
        if i in li:
            date1=i
        else:
            d=d
    li.remove(date1)
    if date1==3:
        if 0 in li:
            date2=0
        else:
            d=d
    else:
        for i in range(1,9):
            if i in li:
                date2=i
            else:
                d=d
            
        
        

    
    li.remove(date2)

    for i in range(3):
        if i in li:
            time1=i
        else:
            d=d
    li.remove(time1)

    for i in range(4):
        if i in li:
            time2=i
        else:
            d=d
    li.remove(time2)

    for i in range(6):
        if i in li:
            time3=i
        else:
            d=d
    li.remove(time3)

    for i in range(10):
        if i in li:
            time4=i
        else:
            d=d
    li.remove(time4)
    if month1!=None and month2!=None and date1!=None and date2!=None and time1!=None and time2!=None and time3!=None and time4!=None:
        print(f"{month1}{month2}/{date1}{date2} {time1}{time2}:{time3}{time4}")
    else:
        print("0")
        

    
        
            
    
         
        
           
            
           
