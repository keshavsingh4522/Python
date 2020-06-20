from collections import Counter as C
s1=input().split()
s2=input().split()
if C(s2)-C(s1)=={}:
    print('Yes')
else:
    print('No')