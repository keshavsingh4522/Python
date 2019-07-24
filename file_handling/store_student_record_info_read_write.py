import pickle
class student:
 def __init__(self,i):
  self.roll=int(input('enter roll number of student {} : '.format(i)))
  self.name=input('enter name of student {} : '.format(i))
 def display(self,pos,sop):
  print('{:<10}{:<10}{:<10}{:<10}'.format(pos,sop,self.roll,self.name))
def DisplayFile():
 file=open('keshav.bin','rb')
 print('{:<10}{:<10}{:<10}{:<10}'.format('pos','sop','self.roll','self.name'))
 try:
  while True:
   #tell: store addres of current cursor
   pos=file.tell()
   #seek: it goes to defined address
   sop=file.seek(pos)
   p=pickle.load(file)
   p.display(pos,sop)
 except Exception as e:
  print(e)
 else:
  file.close()
#writing data in file
try:
 DisplayFile()
 file=open('keshav.bin','ab')
except:
  file=open('keshav.bin','wb')

n=int(input('enter number of student: '))
for i in range(1,n+1):
 s=student(i)
 pickle.dump(s,file)
file.close()
#modifying of data
print('\nmodifying of data\n')
n=int(input('enter roll number'))
file=open('keshav.bin','rb+')
try:
 while True:
  po=file.tell()
  p=pickle.load(file)
  if n==p.roll:
   file.seek(po)
   p.roll=int(input('enter roll number of student {} : '.format(n)))
   p.name=input('enter name number of student {} : '.format(n))
   pickle.dump(p,file)
except:
 file.close()
