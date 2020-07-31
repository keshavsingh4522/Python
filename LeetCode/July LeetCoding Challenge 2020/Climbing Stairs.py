def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def get_p(n,n1,n2):
    return fact(n)//(fact(n1)*fact(n2))

n=int(input())
c_2=n//2
c_1=n%2
sum_p=1
while c_2:
    sum_p+=get_p(c_2+c_1,c_2,c_1)
    c_2-=1
    c_1+=2
print(sum_p)