class Node:
 def __init__(self):
  self.data=None
  self.next=None


class LinkedList:
 def __init__(self):
  self.start=None

 def CreateList(self):
  while True:
   newnode=Node()
   newnode.data=int(input('enter data: '))
   if self.start==None:
    self.start=newnode
    current=newnode
   else:
    current.next=newnode
    current=newnode
   n=input('Enter Your Choice(y/n)')
   if n in ['n','N']:
     break

 def Display(self):
  ptr=self.start
  while ptr!=None:
   print(ptr.data,end='\t')
   ptr=ptr.next


l=LinkedList()
l.CreateList()
l.Display()
'''
output:
enter data: 12
Enter Your Choice(y/n)
enter data: 343
Enter Your Choice(y/n)
enter data: 78
Enter Your Choice(y/n)
enter data: 965
Enter Your Choice(y/n)
enter data: 121
Enter Your Choice(y/n)
enter data: 677
Enter Your Choice(y/n)n
12	343	78	965	121	677	
'''
