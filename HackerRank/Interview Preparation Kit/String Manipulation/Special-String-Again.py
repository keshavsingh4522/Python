n=int(input())
s=input()
count=0
count_sequence=0
prev=''
for i,v in enumerate(s):
    #count single char
    count_sequence+=1
    if i and (prev!=v):
        j=1
        while (i-j)>=0 and (i+j)<len(s) and j<=count_sequence:
            if s[i-j]==prev==s[i+j]:
                count+=1
                j+=1
            else:
                break
        count_sequence=1
    count+=count_sequence
    prev=v
print(count)