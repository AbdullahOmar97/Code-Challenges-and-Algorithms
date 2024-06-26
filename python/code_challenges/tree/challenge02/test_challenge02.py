# Write your test here

# test_challenge02.py

import pytest
from challenge02 import TreeNode, is_same_tree

# Helper function to create binary trees from list representation
def create_tree_from_list(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# Test cases
def test_same_trees():
    p1 = create_tree_from_list([1, 2, 3])
    q1 = create_tree_from_list([1, 2, 3])
    assert is_same_tree(p1, q1) == True

    p2 = create_tree_from_list([1, 2])
    q2 = create_tree_from_list([1, None, 2])
    assert is_same_tree(p2, q2) == False

    p3 = create_tree_from_list([1, 2, 1])
    q3 = create_tree_from_list([1, 1, 2])
    assert is_same_tree(p3, q3) == False

    p4 = create_tree_from_list([1, 2, 3, 4, 5])
    q4 = create_tree_from_list([1, 2, 3, 4, 5])
    assert is_same_tree(p4, q4) == True

def test_empty_trees():
    assert is_same_tree(None, None) == True

def test_one_empty_tree():
    p = create_tree_from_list([1, 2, 3])
    assert is_same_tree(p, None) == False
    assert is_same_tree(None, p) == False

def test_different_structures():
    p = create_tree_from_list([1, 2, 3])
    q = create_tree_from_list([1, 3, 2])
    assert is_same_tree(p, q) == False
