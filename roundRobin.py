at=[]
bt=[]
no=[]
comp_time=[]
tat=[]
wt=[]
rr=[]
c_time={}
completed=[]
first_cpu=[]
got_cpu=[]
ready_queue=[]

n = int(input("Enter the no. of processes: "))
quantum = int(input("Enter the time quantum: "))
print ("Enter arrival time and burst time for processes: ")

enter=[0]*n
for i in range (n):
    ar =int(input())
    at.append(ar)
    bu = int(input())
    bt.append(bu)
    no.append(i)
    completed.append(0)
    got_cpu.append(0)
    first_cpu.append(0)

print("\nProcess Schedule:")
for i in range(0,n):
    for j in range (0,n-1):
        if (at[j]>at[j+1]):
            at[j],at[j+1]=at[j+1],at[j]
            bt[j],bt[j+1]=bt[j+1],bt[j]
            no[j],no[j+1]=no[j+1],no[j]

remain_time=list(bt)
ct = 0
counter=0
flag=0
while(counter!=n):
    if(flag==1):
        j=ready_queue.pop()
    for i in range (0,n):
        if ((at[i]<=ct) & (completed[no[i]]==0)&(enter[no[i]]<1)):
            ready_queue.append(no[i])
            m=no[i]
            enter[m]=enter[m]+1

    if(flag==1):
        ready_queue.append(j)
    if(len(ready_queue)==0):
        print ("\nFor time",ct,"to ",end="")
        ct=ct+1
        print(ct,": ",end="")
        print("IDEAL")
        print()
    else:
        c=ready_queue.pop(0)

        got_cpu[c]=got_cpu[c]+1
        if(got_cpu[c]==1):
            first_cpu[c]=ct
        
        if(remain_time[no.index(c)]>=quantum):
            print ("\nFor time",ct,"to ",end="")
            ct =  ct + quantum
            remain_time[no.index(c)]=remain_time[no.index(c)]-quantum
            print(ct,": ",end="")
        else:
            print ("\nFor time",ct,"to ",end="")
            ct =  ct + remain_time[no.index(c)]
            remain_time[no.index(c)]=0
            print(ct,": ",end="")
        print("Process",c)
        print()
        if(remain_time[no.index(c)]==0):
            c_time.update({c:ct})
            completed[c]=1
            counter=counter+1
            flag=0
        else:
            ready_queue.append(c)
            flag=1

for i in no:
    comp_time.append(c_time.get(i))

total_wt=0 
total_tat=0
print("\nP.No \t AT \t BT \t CT \t TAT \t WT \t RT")
for i in range(n):
    tat.append(comp_time[i]-at[i])
    wt.append(tat[i]-bt[i])
    rr.append(first_cpu[no[i]]-at[i])
    total_wt= total_wt+wt[i]
    total_tat=total_tat+tat[i]
    print("{} \t {} \t {} \t {} \t {} \t {} \t {}".format(no[i],at[i],bt[i],comp_time[i],tat[i],wt[i],rr[i]))

print("\nTotal average turn-around time:{}".format(total_tat/n))
print("Total average waiting time:{}".format(total_wt/n))
print("Throughput: {}".format(n/ct))