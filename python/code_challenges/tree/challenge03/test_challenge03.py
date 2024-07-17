import unittest
from challenge03 import sortedArrayToBST, TreeNode

def inorder_traversal(root):
    """
    Helper function to perform inorder traversal of the BST.
    """
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

class TestSortedArrayToBST(unittest.TestCase):
    def test_example1(self):
        nums = [0, -3, -10, 5, 9]
        print("before: " + str(nums))
        nums.sort()  # Make sure the array is sorted
        bst = sortedArrayToBST(nums)
        result = inorder_traversal(bst)
        print("after: " + str(result))
        self.assertEqual(result, nums)

    def test_example2(self):
        nums = [3, 1]
        print("before: " + str(nums))
        nums.sort()  # Make sure the array is sorted
        bst = sortedArrayToBST(nums)
        result = inorder_traversal(bst)
        print("after: " + str(result))
        self.assertEqual(result, nums)

if __name__ == "__main__":
    unittest.main()
