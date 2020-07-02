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
def compare(l1,l2):
    ptr1=l1.start
    ptr2=l2.start
    while ptr1 and ptr2:
        if ptr1.data!=ptr2.data:
            return 0
        ptr1=ptr1.next
        ptr2=ptr2.next
    if ptr1 is None and ptr2 is None:
        return 1
    else:
        return 0
def addElemntInLinkedList():
    l=LinkedList()
    for i in range(int(input())):
        n=int(input())
        if l .start==None:
            l.start=node(n)
            ptr=l.start
        else:
            ptr.next=node(n)
            ptr=ptr.next
    return l
for _ in range(int(input())):
    l1=addElemntInLinkedList()
    l2=addElemntInLinkedList()
    print(compare(l1,l2))