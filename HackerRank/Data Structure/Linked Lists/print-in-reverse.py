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
    def display_reverse(self,head):
        if head:
            self.display_reverse(head.next)
            print(head.data)
    def InsertAtHead(self,n):
        if self.start is None:
            self.start=node(n)
        else:
            temp=self.start
            self.start=node(n)
            self.start.next=temp
l=LinkedList()
for _ in range(int(input())):
    n=int(input())
    if l .start==None:
        l.start=node(n)
        ptr=l.start
    else:
        ptr.next=node(n)
        ptr=ptr.next
l.display_reverse(l.start)