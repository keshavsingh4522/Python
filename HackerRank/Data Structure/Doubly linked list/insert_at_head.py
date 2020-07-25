class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.start=None

# display data
def display(head):
    while head:
        print(head.data,end=' ')
        tail=head.prev
        head=head.next
        
# insert at head
def insert_at_head(a):
    dl=doubly_linked_list()
    temp=None
    for i in a:
        if not temp:
            temp=node(i)
        else:
            temp.prev=node(i)
            temp.prev.next=temp
            temp=temp.prev
    dl.start=temp
    return dl.start

print('Enter data at a time following by space')
head=insert_at_head(map(int,input().split()))
print('after adding data at head the doubly linked list look like as below')
display(head)
print()