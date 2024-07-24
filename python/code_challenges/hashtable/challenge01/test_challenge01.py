# Write your test here
# test_challenge01.py

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
    assert result, "Expected two nodes to sum up to 9"
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
    assert not result, "Expected no two nodes to sum up to 4"
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
    assert not result, "Expected no two nodes to sum up to 5 in an empty tree"
    print("test_empty_tree passed\n")

def main():
    test_example_1()
    test_example_2()
    test_empty_tree()

if __name__ == "__main__":
    main()
