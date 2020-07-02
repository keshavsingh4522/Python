class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def display(self):
        if self.start==None:
            print('list is empty')
        else:
            temp=self.start
            while temp:
                print(temp.data)
                temp=temp.next
    def InsertAtHead(self,n):
        if self.start is None:
            self.start=node(n)
        else:
            temp=self.start
            self.start=node(n)
            self.start.next=temp
l=LinkedList()
for i in range(int(input())):
    n=int(input())
    if i==0:
        l.start=node(n)
        ptr=l.start
    else:
        ptr.next=node(n)
        ptr=ptr.next