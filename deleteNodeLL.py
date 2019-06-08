# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Given linked list -- head = [4,5,1,9], which looks like following:



 

# Example 1:

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:

# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

class ListNode:

    def __init__(self, x):
        self.data = x
        self.next = None
#since we only access node x, then we shall cpopy the content of 
# the next node into nodex and remove the next node
def deleteNode(x):
	x.data = x.next.data
	x.next = x.next.next

# Qn2. remove duplicates from an unsorted ll

def remove(head):
	curr = head
	container = set()
	while curr:
		if curr.data in container:
			curr.data = curr.next.data
			curr.next =curr.next.next
			curr=curr.next

		else:
			container.add(curr.data)
			curr = curr.next

# Qn3. return kth to last
# will have two pointers moving at diff speeds

def kth(head, k):
	slow = head
	for i in range(k):
		fast = slow.next

	while fast:
		fast = fast.next
		slow = slow.next


	return slow



# Qn3. reverse a ll

# Python program to reverse a linked list  
# Time Complexity : O(n) 
# Space Complexity : O(1) 
  
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
  
    # Function to reverse the linked list 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current
	    current = next
        self.head = prev # you can also just return Prev
          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next
  
	
	













