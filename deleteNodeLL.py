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

# Qn3. remove duplicates from an unsorted ll
