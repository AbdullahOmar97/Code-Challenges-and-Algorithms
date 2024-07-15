import unittest
from challenge03 import sortedArrayToBST, TreeNode

class TestSortedArrayToBST(unittest.TestCase):

    def setUp(self):
        # Initialize any necessary setup for tests
        pass

    def test_sortedArrayToBST_example1(self):
        nums = [0, -3, -10, 5, 9]
        expected_tree = TreeNode(0)
        expected_tree.left = TreeNode(-3)
        expected_tree.right = TreeNode(9)
        expected_tree.left.left = TreeNode(-10)
        expected_tree.right.right = TreeNode(5)
        
        actual_tree = sortedArrayToBST(nums)
        
        self.assertTrue(self.trees_are_equal(actual_tree, expected_tree))
        print(f"Example 1: Expected BST: {self.tree_to_list(expected_tree)}")
        print(f"Example 1: Actual BST: {self.tree_to_list(actual_tree)}")

    def test_sortedArrayToBST_example2(self):
        nums = [3, 1]
        expected_tree = TreeNode(3)
        expected_tree.left = TreeNode(1)
        
        actual_tree = sortedArrayToBST(nums)
        
        self.assertTrue(self.trees_are_equal(actual_tree, expected_tree))
        print(f"Example 2: Expected BST: {self.tree_to_list(expected_tree)}")
        print(f"Example 2: Actual BST: {self.tree_to_list(actual_tree)}")

    def trees_are_equal(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return (self.trees_are_equal(tree1.left, tree2.left) and
                self.trees_are_equal(tree1.right, tree2.right))

    def tree_to_list(self, root):
        """
        Convert a binary tree into a list representation for easier comparison.
        """
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
        return result

if __name__ == '__main__':
    unittest.main()

