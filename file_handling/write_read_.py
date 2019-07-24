file=open('keshav.txt','w')
while True:
 try:
  l=input('write in file: ')
  file.write(l+'\n')
  n=input('enter your choise:(y/n)')
  if n in ('y','Y'):
   continue
  if n in ('n','N'):
   break
 except Exception as e:
  print(e)
file.close()
l=open('keshav.txt','r')
print(l.readlines())
l.close()
