# Write here the code challenge solution

# challenge01.py

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    # The first element of preorder is the root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder list
    root_index_in_inorder = inorder.index(root_val)

    # Elements to the left of the root_index_in_inorder in inorder are the left subtree
    left_inorder = inorder[:root_index_in_inorder]
    # Elements to the right of the root_index_in_inorder in inorder are the right subtree
    right_inorder = inorder[root_index_in_inorder + 1:]

    # Elements in the preorder list corresponding to the left subtree
    left_preorder = preorder[1:1 + len(left_inorder)]
    # Elements in the preorder list corresponding to the right subtree
    right_preorder = preorder[1 + len(left_inorder):]

    # Recursively construct the left and right subtree
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root
