import pickle
import os
class Account:
 def __init__(self,id=10000000):
  self.type=input('what type of Account you Want to open? S(min 5000) or C(min 10000) :').upper()
  self.name=input('Enter name: ')
  self.id=id
  while True:
   self.amount=int(input('Enter Amount: '))
   if self.type in ('s','S'):
    if self.amount<5000:
     print('Enter Amount Again')
     continue
    else:
     break
   if self.type in ('c','C'):
    if self.amount<10000:
     print('Enter Amount Again')
     continue
    else:
     break
 def display(self):
  print('{:<20}{:<20}{:<20}{:<20}'.format(self.id,self.name,self.type,self.amount))
#create account
def CreateAccount():
 try:
  file=open('keshav.bin','rb')
  while True:
   p=pickle.load(file)
 except FileNotFoundError as e:
  file1=open('keshav.bin','ab')
  s=Account()
  pickle.dump(s,file1)
  file1.close()
 except EOFError as e:
  file1=open('keshav.bin','ab')
  p.id+=1
  print(p.id)
  s=Account(p.id)
  pickle.dump(s,file1)
  file1.close()
#display function
def DisplayFile():
 file=open('keshav.bin','rb')
 print('{:<20}{:<20}{:<20}{:<20}'.format('id','name','type','amount'))
 try:
  while True:
   p=pickle.load(file)
   p.display()
 except Exception as e:
  print(e)
 else:
  file.close()
#deposit money
def Deposit():
 file=open('keshav.bin','rb+')
 file1=open('temp.bin','wb')
 n=int(input('enter id ex. 10000000: '))
 money=int(input('enter money to deposit: '))
 try:
  while True:
   p=pickle.load(file)
   if p.id==n:
     p.amount+=money
   pickle.dump(p,file1)
 except:
  file.close()
  file1.close()
 finally:
  os.remove('keshav.bin')
  os.rename('temp.bin','keshav.bin')

#withdraw money
def Withdraw():
 def main_money():
  def avail_money():
   money=int(input('enter money in multiple of 100 200 500 2000: '))
   l=[100,200,500,2000]
   for i in l:
    if money%i==0:
     return money
    else:
     continue
   else:
    print("u cant withdraw money ")
    return False
  while True:
   r=avail_money()
   if r==False:
    print('failed')
    continue
   else:
    return r

 def load_money(file,file1):
  while True:
   p=pickle.load(file)
   if p.id==n:
    while True:
     money=main_money()
     if p.amount<money:
      print("insufficient balance!")
      continue
     else:
      if p.type=='C':
       if p.amount-money>=10000:
        p.amount-=money
        print('process completed successfully !')
        break
       else:
        print("\t can't withdraw money","\n\t your current account limit is 10000","\n\t you can withraw max: ",p.amount-10000)
        continue
      if p.type=='S':
       if p.amount-money>=5000:
        p.amount-=money
        print('process completed successfully !')
        break
       else:
        print("\tcan't withdraw","\n\t your current account limit is 5000","\n\t you can withraw max: ",p.amount-5000)
        continue
   pickle.dump(p,file1)
 file=open('keshav.bin','rb+')
 file1=open('temp.bin','wb')
 n=int(input('enter id ex. 10000000: '))
 try:
  load_money(file,file1)
 except:
  file.close()
  file1.close()
 finally:
  os.remove('keshav.bin')
  os.rename('temp.bin','keshav.bin')
#update your account
def Update():
 file=open('keshav.bin','rb+')
 file1=open('temp.bin','wb')
 n=int(input('enter id ex. 10000000: '))
 name=input('Enter new name:  ')
 #type=input('Enter type of account: ').upper()
 try:
  while True:
   p=pickle.load(file)
   if p.id==n:
     p.name=name
   pickle.dump(p,file1)
 except:
  file.close()
  file1.close()
 finally:
  os.remove('keshav.bin')
  os.rename('temp.bin','keshav.bin')
#search your account
def Search():
 file=open('keshav.bin','rb')
 n=int(input('enter id ex. 10000000: '))
 try:
  while True:
   p=pickle.load(file)
   if p.id==n:
     print(' {:*>35} {:*<35}'.format('start detail of account: ',p.name))
     print('id: ',p.id,'\nname: ',p.name,'\ntotal balance: ',p.amount,'\ntype: ',p.type)
     print(' {:*>35} {:*<35}'.format(' end detail of account: ',p.name))
     break
 except:
  file.close()
 else:
  file.close()
#
print("{:*^70}".format(' Banking Management System '),end='\n'*3)
def Choise():
 print('What Do You Wanna Do?')
 print('1.Create Account')
 print('2.View all Accounts')
 print('3.Deposit')
 print('4.Withdraw')
 print('5.Update')
 print('6.Search')
 print('7.Exit')
 return int(input('Enter your choise here: '))
while True:
 i=Choise()
 if i==1:
  CreateAccount()
 if i==2:
  DisplayFile()
 if i==3:
  Deposit()
 if i==4:
  Withdraw()
 if i==5:
  Update()
 if i==6:
  Search()
 if i==7:
  break
