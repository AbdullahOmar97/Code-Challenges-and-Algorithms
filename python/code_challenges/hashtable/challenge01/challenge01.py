# Write here the code challenge solution

# challenge01.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def two_sum_bst(root, k):
    """
    Checks if there exists a pair in the BST whose sum equals the target sum (k).

    Args:
        root: The root node of the Binary Search Tree.
        k: The target sum.

    Returns:
        True if there exists a pair that sums to k, False otherwise.
    """
    seen = set()

    def dfs(node):
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)

    return dfs(root)
