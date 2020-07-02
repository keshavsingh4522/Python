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
    def deleteNode(self, position):
        # if linked ist is empty
        temp=self.start
        if temp==None:
            return
        
        # if heads to be removed
        if position==0:
            self.start=temp.next
            temp=None
            return
        
        #iterate nodes for deletion
        for  i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        
        #if position>length of linked list
        if temp is None:
            return
        if temp.next is None:
            return
        
        next=temp.next.next
        temp.next=None
        temp.next=next
        
l=LinkedList()
for i in range(int(input())):
    n=int(input())
    if i==0:
        l.start=node(n)
        ptr=l.start
    else:
        ptr.next=node(n)
        ptr=ptr.next