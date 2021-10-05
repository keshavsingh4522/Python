input1=int(input("enter the total no of seconds :"))

if input1>=60:
    mn=input1//60
    sec=input1%60
    if mn>=60:
        hrs=mn//60
        mn=mn%60
print(" hours :"+str(hrs)+" minutes :"+str(mn)+" seconds :"+str(sec))

#enter the total no of seconds :562
#hours :1 minutes :9 seconds :22
