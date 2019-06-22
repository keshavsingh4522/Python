r,c=map(int,input('enter number of rows and columns of matrix: ').split())
m1=[]
m2=[]
a=[]
print('<<<<< enter element of matrix1 >>>>>')
for i in range(r):
 l=[]
 for j in range(c):
  l.append(int(input(f"enter in m1[{i}][{j}]: ")))
 m1.append(l)

print('<<<<< enter element of matrix2 >>>>>')
for i in range(r):
 l=[]
 for j in range(c):
  l.append(int(input(f"enter in m2[{i}][{j}]: ")))
 m2.append(l)

#addition of two matrix
print('<<<<< addition of two matrix >>>>>')
for i in range(r):
   l=[]
   for j in range(c):
    l.append(int(m1[i][j])+int(m2[i][j]))
   a.append(l)
print(a)
'''
output:
enter number of rows and columns of matrix: 2 2
<<<<< enter element of matrix1 >>>>>
enter in m1[0][0]: 21
enter in m1[0][1]: 22
enter in m1[1][0]: 23
enter in m1[1][1]: 24
<<<<< enter element of matrix2 >>>>>
enter in m2[0][0]: 1
enter in m2[0][1]: 2
enter in m2[1][0]: 3
enter in m2[1][1]: 4
<<<<< addition of two matrix >>>>>
[[22, 24], [26, 28]]
'''
