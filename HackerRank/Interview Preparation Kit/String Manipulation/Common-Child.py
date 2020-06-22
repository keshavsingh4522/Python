s1=input()
s2=input()
l=[[0]*len(s2) for i in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        if i==0 or j==0:
            if s1[i]==s2[j]:
                l[i][j]=1
        else:
            if s1[i]==s2[j]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
l