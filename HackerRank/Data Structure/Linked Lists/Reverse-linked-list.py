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
    def reversing_linked_list(self):
        current=self.start
        previous=None
        while current:
            temp=current.next
            current.next=previous
            previous=current
            current=temp
        self.start=previous
                
l=LinkedList()
for _ in range(int(input())):
    n=int(input())
    if l .start==None:
        l.start=node(n)
        ptr=l.start
    else:
        ptr.next=node(n)
        ptr=ptr.next
print('Linked Lists')
l.display()
print('Linked Lists After Reversing')
l.reversing_linked_list()
l.display()