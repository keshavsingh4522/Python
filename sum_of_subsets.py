#Sum of subsets problem in python.

b=[]
def solution(a,n,subset,s):
 global ctr
 ctr=0
 if s==0:
 b.append(subset)
 return
 if n==0:
 return
 if a[n-1]<=s:
 solution(a,n-1,subset,s)
 solution(a,n-1,subset+str(a[n-1])+" ",s-a[n-1])
 else:
 solution(a,n-1,subset,s)
print("Enter the list of integers",end=":")
a=[int(x) for x in input().split()]
s=int(input("Enter the sum value:"))
subset=""
solution(a,len(a),subset,s)
ctr=1
for i in b:
 print("Solution",ctr,"---->",i)
 ctr=ctr+1
print("The total number of solution for sum of subsets is",len(b))
