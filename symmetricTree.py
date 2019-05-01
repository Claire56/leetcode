# Given a binary tree, check whether it is a mirror of 
# itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

def symmetric(root):
	# Edge case.
        if not root:
            return True
        
        # Initialize two stacks to compare mirror traversals.
        stack_left = [root]
        stack_right = [root]
        
        while stack_left and stack_right:
            
            # Pop a node from left-first traversal
            current_left = stack_left.pop()
            
            # Pop a node from right-first traversal
            current_right = stack_right.pop()
            
            # Compare the nodes; difference means broken symmetry.
            if current_left.val != current_right.val:
                return False
            
            # Go left in the left-first
            if current_left.left:
                
                # But if we can't go right in the right-first,
                # it means broken symmetry.
                if not current_right.right:
                    return False
                
                # Append to respective stacks symmetrically.
                stack_left.append(current_left.left)
                stack_right.append(current_right.right)
            
            # Then go right in the left-first.
            if current_left.right:
                
                # But if we can't go left in the right-first,
                # it means broken symmetry.
                if not current_right.left:
                    return False
                
                # Append to respective stacks symmetrically.
                stack_left.append(current_left.right)
                stack_right.append(current_right.left)
        
        # Make sure we traversed the whole tree both ways.
        return stack_left == [] and stack_right == []






	



