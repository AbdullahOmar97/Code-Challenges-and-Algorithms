# Write here the code challenge solution

class TreeNode:
    """
    Class representing a node in a binary tree.

    Attributes:
    val (int): The value of the node.
    left (TreeNode, optional): A reference to the left child node.
    right (TreeNode, optional): A reference to the right child node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_max_in_bst(root):
    """
    Finds the maximum value in a binary tree using inorder traversal.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    int: The maximum value found in the binary tree.
    """
    def inorder_traversal(node):
        """
        Helper function to perform inorder traversal (right, root, left).

        Args:
        node (TreeNode): The current node being visited in the traversal.
        """
        nonlocal max_value
        if node:
            # Traverse right subtree
            inorder_traversal(node.right)
            # Visit the node itself
            if node.val > max_value:
                max_value = node.val
            # Traverse left subtree
            inorder_traversal(node.left)
    
    # Initialize max_value to negative infinity
    max_value = float('-inf')
    
    # Start the inorder traversal
    inorder_traversal(root)
    
    return max_value

