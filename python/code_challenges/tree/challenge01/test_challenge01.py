# test_challenge01.py

import pytest
from challenge01 import buildTree, TreeNode

def tree_to_list(root):
    """Helper function to convert tree to list (level-order)"""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result

def test_buildTree():
    # Example 1
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    result = tree_to_list(root)
    expected = [3, 9, 20, None, None, 15, 7]
    print(f"Preorder: {preorder}, Inorder: {inorder}, Result: {result}, Expected: {expected}")
    assert result == expected

    # Example 2
    preorder = [-1]
    inorder = [-1]
    root = buildTree(preorder, inorder)
    result = tree_to_list(root)
    expected = [-1]
    print(f"Preorder: {preorder}, Inorder: {inorder}, Result: {result}, Expected: {expected}")
    assert result == expected

    # Additional test case
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    root = buildTree(preorder, inorder)
    result = tree_to_list(root)
    expected = [1, 2, 3, 4, 5, 6, 7]
    print(f"Preorder: {preorder}, Inorder: {inorder}, Result: {result}, Expected: {expected}")
    assert result == expected

if __name__ == "__main__":
    pytest.main(["-s", __file__])
