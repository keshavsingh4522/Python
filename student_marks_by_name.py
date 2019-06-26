n=int(input('enter no of student to store thier details: '))
d={}
for i in range(n):
 name,*marks=input('enter name marks of p c m: ').split()
 marks=list(map(float,marks))
 d[name]=marks
q=input('enter student name: ')
t=sum(d[q])/3
print(q,' %.2f'%t)
