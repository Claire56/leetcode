# Implement a Queue - Using Two Stacks - 

# Solution
# The key insight is that a stack reverses order (while a queue
#  doesn't). A sequence of elements pushed on a stack comes back
# in reversed order when popped. Consequently, two stacks chained
#  together will return elements in the same order, since reversed
#   order reversed again is original order.

# We use an in-stack that we fill when an element is enqueued 
# and the dequeue operation takes elements from an out-stack.
#  If the out-stack is empty we pop all elements from the in-stack 
#  and push them onto the out-stack.


 class qfromStacks:
 	 def __init__(self):
 	 	self.stack_in = []
 	 	self.stack_out=[]

 	 def enqueue(self, item):
 	 	self.stack_in.append(item)


 	 def dequeue(self):
 	 	if not self.stack_out:
 	 		while self.stack_in:
 	 			self.stack_out.append(self.stack_in.pop())
 	 	return self.stack_out.pop()
