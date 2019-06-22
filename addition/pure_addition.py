r,c=map(int,input('enter number of rows and columns of matrix: ').split())
add=[]
print('<<<<< enter element of matrix1 >>>>>')
for i in range(r):
 la=[]
 for j in range(c):
  a,b=map(int,input(f"enter in m1[{i}][{j}] m2[{i}][{j}]: ").split())
  la.append(a+b)
 add.append(la)

print('\naddition of two matrix is: ',add,sep='')
'''
output:
enter number of rows and columns of matrix: 2 2
<<<<< enter element of matrix1 >>>>>
enter in m1[0][0] m2[0][0]: 12 13
enter in m1[0][1] m2[0][1]: 22 26
enter in m1[1][0] m2[1][0]: 89 45
enter in m1[1][1] m2[1][1]: 40 70

addition of two matrix is: [[25, 48], [134, 110]]
'''
