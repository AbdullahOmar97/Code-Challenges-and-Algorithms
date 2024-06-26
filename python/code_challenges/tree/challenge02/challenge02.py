# Write here the code challenge solution

# challenge02.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    from collections import deque
    
    # Helper function for breadth-first traversal
    def bfs(root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)  # Representing null nodes explicitly
        return result
    
    # Perform breadth-first traversal on both trees
    p_values = bfs(p)
    q_values = bfs(q)
    
    # Compare the traversal results
    return p_values == q_values
