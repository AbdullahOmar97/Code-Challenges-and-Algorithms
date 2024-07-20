# Write your test here

import unittest
from challenge05 import find_max_height

class TestFindMaxHeight(unittest.TestCase):
    def test_example_case(self):
        """
        Test the example case provided in the problem description.
        """
        tree = [10, 20, 30, 40, 28, 27, 50, 29]
        print(f'The Tree is: {tree}')
        result = find_max_height(tree)
        print(f"Test Example Case: Result = {result}")
        self.assertEqual(result, 3)

    def test_empty_tree(self):
        """
        Test the case of an empty tree.
        """
        tree = []
        print(f'The Tree is: {tree}')
        result = find_max_height(tree)
        print(f"Test Empty Tree: Result = {result}")
        self.assertEqual(result, -1)  # Height of an empty tree should be -1

    def test_single_node(self):
        """
        Test the case of a single-node tree.
        """
        tree = [1]
        print(f'The Tree is: {tree}')
        result = find_max_height(tree)
        print(f"Test Single Node: Result = {result}")
        self.assertEqual(result, 0)  # Height of a single node tree is 0

    def test_two_levels(self):
        """
        Test a tree with two levels.
        """
        tree = [1, 2, 3]
        print(f'The Tree is: {tree}')
        result = find_max_height(tree)
        print(f"Test Two Levels: Result = {result}")
        self.assertEqual(result, 1)  # Tree with two levels should have height 1

    def test_three_levels(self):
        """
        Test a tree with three levels.
        """
        tree = [1, 2, 3, 4, 5, 6, 7]
        print(f'The Tree is: {tree}')
        result = find_max_height(tree)
        print(f"Test Three Levels: Result = {result}")
        self.assertEqual(result, 2)  # Tree with three levels should have height 2

if __name__ == '__main__':
    unittest.main(verbosity=2)
