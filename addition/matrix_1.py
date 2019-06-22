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
   for j in range(c):
    a.append(int(m1[i][j])+int(m2[i][j]))
print(a)
'''
output:
enter number of rows and columns of matrix: 2 2
<<<<< enter element of matrix1 >>>>>
enter in m1[0][0]: 22
enter in m1[0][1]: 11
enter in m1[1][0]: 22
enter in m1[1][1]: 33
<<<<< enter element of matrix2 >>>>>
enter in m2[0][0]: 21
enter in m2[0][1]: 33
enter in m2[1][0]: 45
enter in m2[1][1]: 33
<<<<< addition of two matrix >>>>>
[43, 44, 67, 66]
'''
