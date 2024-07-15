# Write here the code challenge solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        TreeNode constructor to initialize a node in a binary tree.

        Args:
        - val (int): The value to be stored in the node.
        - left (TreeNode, optional): Reference to the left child node.
        - right (TreeNode, optional): Reference to the right child node.
        """
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    Convert a sorted array into a height-balanced binary search tree (BST).

    Args:
    - nums (List[int]): A sorted array of unique integers.

    Returns:
    - TreeNode: The root node of the resulting BST.

    Example:
    >>> nums = [0, -3, -10, 5, 9]
    >>> root = sortedArrayToBST(nums)
    >>> # The resulting tree will be [0, -3, 9, -10, None, 5]
    """
    def sortedArrayToBSTHelper(left, right):
        """
        A helper function to recursively build a balanced BST from a sorted array.

        Args:
        - left (int): The left index of the current subarray.
        - right (int): The right index of the current subarray.

        Returns:
        - TreeNode or None: The root node of the constructed BST subtree.
        """
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBSTHelper(left, mid - 1)
        root.right = sortedArrayToBSTHelper(mid + 1, right)
        return root
    
    return sortedArrayToBSTHelper(0, len(nums) - 1)
