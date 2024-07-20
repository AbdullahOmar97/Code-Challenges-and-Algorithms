# Write your test here

import unittest

from challenge04 import *


class TestFindMaxInBST(unittest.TestCase):

    def setUp(self):
        print(f"\nRunning test: {self._testMethodName}")

    def test_single_node(self):
        root = TreeNode(10)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, 10)

    def test_left_skewed_tree(self):
        # Tree: 3 <- 2 <- 1
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, 3)

    def test_right_skewed_tree(self):
        # Tree: 1 -> 2 -> 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, 3)

    def test_balanced_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, 3)

    def test_complex_tree(self):
        root = TreeNode(1000)
        root.left = TreeNode(500)
        root.right = TreeNode(2000)
        root.left.left = TreeNode(250)
        root.left.right = TreeNode(600)
        root.right.right = TreeNode(12000)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, 12000)

    def test_all_negative_values(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, -1)

    def test_mixed_values(self):
        root = TreeNode(0)
        root.left = TreeNode(-1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(-3)
        root.left.right = TreeNode(-2)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(3)
        result = find_max_in_bst(root)
        print(f"Test result: {result}")
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
