class Node:
    def __init__(self):
        self.data=None
        self.next=None
class Linked_List(Node):
    def __init__(self):
        self.start=None
    def Create(self):
        while True:
            newnode=Node()
            newnode.data=int(input("Enter data part : "))
            if self.start==None:
                self.start=newnode
                current=newnode
            else:
                current.next=newnode
                current=newnode
            char=input("DO YOU WANT TO ENTER MORE NODES? : ")
            if char in ('n','N'):
                break
    def Display(self):
        ptr=self.start
        print("\n\nDATA IS AS FOLLOWS : \n")
        while ptr!=None:
            print(ptr.data,end=' ')
            ptr=ptr.next
        print()

    def Reverse(self,ptr):
        if ptr==None:
            return
        self.Reverse(ptr.next)
        print(ptr.data)

l1=Linked_List()
l1.Create()
l1.Display()
l1.Reverse(l1.start)
