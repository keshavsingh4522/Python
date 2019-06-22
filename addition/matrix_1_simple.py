r,c=map(int,input('enter number of rows and columns of matrix: ').split())
m1=[]
m2=[]
add=[]
print('<<<<< enter element of matrix1 >>>>>')
for i in range(r):
 l1=[]
 l2=[]
 la=[]
 for j in range(c):
  a,b=map(int,input(f"enter in m1[{i}][{j}] m2[{i}][{j}]: ").split())
  l1.append(a)
  l2.append(b)
  la.append(a+b)
 m1.append(l1)
 m2.append(l2)
 add.append(la)

print('matrix1 : ',m1,'\nmatrix2 : ',m2,'\naddition: ',add,sep='')
'''
output:
enter number of rows and columns of matrix: 2 2
<<<<< enter element of matrix1 >>>>>
enter in m1[0][0] m2[0][0]: 1 2
enter in m1[0][1] m2[0][1]: 3 4
enter in m1[1][0] m2[1][0]: 5 6
enter in m1[1][1] m2[1][1]: 7 8
matrix1 : [[1, 3], [5, 7]]
matrix2 : [[2, 4], [6, 8]]
addition: [[3, 7], [11, 15]]
'''
