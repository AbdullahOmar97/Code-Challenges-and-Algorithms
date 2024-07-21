# Write your test here
# test_challenge01.py

import pytest
from challenge01 import TreeNode, two_sum_bst

def test_example_1():
    print("Starting test_example_1")
    print("Creating the tree:")
    root = TreeNode(
        7,
        TreeNode(2, TreeNode(1), TreeNode(5)),
        TreeNode(9, None, TreeNode(14))
    )
    print("Tree created.")
    k = 9
    print(f"Testing for k = {k}")
    result = two_sum_bst(root, k)
    print(f"Result: {result}")
    assert result
    print("test_example_1 passed\n")

def test_example_2():
    print("Starting test_example_2")
    print("Creating the tree:")
    root = TreeNode(
        7,
        TreeNode(2, TreeNode(1), TreeNode(5)),
        TreeNode(9, None, TreeNode(14))
    )
    print("Tree created.")
    k = 4
    print(f"Testing for k = {k}")
    result = two_sum_bst(root, k)
    print(f"Result: {result}")
    assert not result
    print("test_example_2 passed\n")

def test_empty_tree():
    print("Starting test_empty_tree")
    print("Creating an empty tree")
    root = None
    print("Empty tree created.")
    k = 5
    print(f"Testing for k = {k}")
    result = two_sum_bst(root, k)
    print(f"Result: {result}")
    assert not result
    print("test_empty_tree passed\n")
