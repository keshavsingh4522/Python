class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
def display(head):
    if head==None:
        print('list is empty')
    else:
        temp=head
        while temp:
            print(temp.data)
            temp=temp.next

def merge(l1,l2):
    l=LinkedList()
    ptr=l
    while l1 or l2:
        if l1 is None:
            ptr.next=l2
            break
        elif l2 is None:
            ptr.next=l1
            break
        else:
            if l1.data>l2.data:
                ptr.next=l2
                l2=l2.next
            else:
                ptr.next=l1
                l1=l1.next
            ptr=ptr.next
    return l.next
#     if l1 is None and l2 is None:
#         return None
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#     if l1.data>l2.data:
#         l=l2
#         l.next=merge(l1,l2.next)
#     else:
#         l=l1
#         l.next=merge(l1.next,l2)
#     return l
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
    return l.start
for _ in range(int(input())):
    l1=addElemntInLinkedList()
    l2=addElemntInLinkedList()
    display(merge(l1,l2))