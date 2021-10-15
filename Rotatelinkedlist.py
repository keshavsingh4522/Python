# Python program to rotate a linked list

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		# allocate node and put the data
		new_node = Node(new_data)

		# Make next of new node as head
		new_node.next = self.head
		
		# move the head to point to the new Node
		self.head = new_node

	# Utility function to print it the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next

	# This function rotates a linked list counter-clockwise and
	# updates the head. The function assumes that k is smaller
	# than size of linked list. It doesn't modify the list if
	# k is greater than of equal to size
	def rotate(self, k):
		if k == 0:
			return
		
		# Let us understand the below code for example k = 4
		# and list = 10->20->30->40->50->60
		current = self.head
		
		# current will either point to kth or NULL after
		# this loop
		# current will point to node 40 in the above example
		count = 1
		while(count <k and current is not None):
			current = current.next
			count += 1
	
		# If current is None, k is greater than or equal
		# to count of nodes in linked list. Don't change
		# the list in this case
		if current is None:
			return

		# current points to kth node. Store it in a variable
		# kth node points to node 40 in the above example
		kthNode = current
	
		# current will point to lsat node after this loop
		# current will point to node 60 in above example
		while(current.next is not None):
			current = current.next

		# Change next of last node to previous head
		# Next of 60 is now changed to node 10
		current.next = self.head
		
		# Change head to (k + 1)th node
		# head is not changed to node 50
		self.head = kthNode.next

		# change next of kth node to NULL
		# next of 40 is not NULL
		kthNode.next = None



# Driver program to test above function
llist = LinkedList()

# Create a list 10->20->30->40->50->60
for i in range(60, 0, -10):
	llist.push(i)

print "Given linked list"
llist.printList()
llist.rotate(4)

print "\nRotated Linked list"
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
