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
        
# insert at tail
def insert_at_tail(a):
    dl=doubly_linked_list()
    for i in a:
        if dl.start==None:
            dl.start=node(i)
            ptr=dl.start
        else:
            ptr.next=node(i)
            ptr.next.prev=ptr
            ptr=ptr.next
    return dl.start

def sortedInsert(head,data):
    temp=node(data)
    if head is None:
        head=node(data)
    else:
        cur=head
        if head.data>data: ##insert temp to head
            temp.next=cur
            cur.prev=temp
            return temp
        else:
            while cur.next!=None:
                if cur.data<data and cur.next.data>=data: # insert temp to non-head part of list
                    temp.next=cur.next
                    temp.prev=cur
                    cur.next.prev=temp
                    cur.next=temp
                    return head
                cur=cur.next
            cur.next=temp # insert temp to end of head
            temp.prev=cur
    return head

print('Enter data at a time following by space')
head=insert_at_tail(map(int,input().split()))
print('after adding data at tail the doubly linked list look like as below')
display(head)
print()
display(sortedInsert(head,int(input('Enter data: '))))