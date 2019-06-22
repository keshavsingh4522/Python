r,c=map(int,input('enter number of rows and columns: ').split())
m=[]
for i in range(r):
 l=[]
 for j in range(c):
  l.append(int(input(f"enter in l[{i}][{j}]: ")))
 m.append(l)
print(m,end='\n\n')

for  row in m:
  print(row)

print(end='\n\n')
for row in m:
 for e in row:
  print(e,end='\t')
'''
output:
enter number of rows and columns: 2 3
enter in l[0][0]: 111 
enter in l[0][1]: 33
enter in l[0][2]: 222
enter in l[1][0]: 5555
enter in l[1][1]: 33
enter in l[1][2]: 555
[[111, 33, 222], [5555, 33, 555]]

[111, 33, 222]
[5555, 33, 555]


111	33	222	5555	33	555	
'''
