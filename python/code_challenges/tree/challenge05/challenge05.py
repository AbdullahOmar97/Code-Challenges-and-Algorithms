# Write here the code challenge solution

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initialize a TreeNode.

        :param value: Value of the node.
        :param left: Left child of the node.
        :param right: Right child of the node.
        """
        self.value = value
        self.left = left
        self.right = right

def build_tree_from_level_order(level_order):
    """
    Build a binary tree from a level-order traversal list.

    :param level_order: List of values in level-order.
    :return: Root node of the constructed binary tree.
    """
    if not level_order:
        return None
    
    root = TreeNode(level_order[0])
    queue = [root]
    index = 1
    
    while queue and index < len(level_order):
        node = queue.pop(0)
        if index < len(level_order):
            node.left = TreeNode(level_order[index])
            queue.append(node.left)
            index += 1
        if index < len(level_order):
            node.right = TreeNode(level_order[index])
            queue.append(node.right)
            index += 1
    
    return root

def max_height(node):
    """
    Compute the height of the binary tree.

    :param node: Root node of the binary tree.
    :return: Height of the tree, defined as the number of edges on the longest path from the root to a leaf.
    """
    if not node:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1

def find_max_height(tree):
    """
    Find the maximum height of a binary tree given its level-order traversal list.

    :param tree: List of values representing the level-order traversal of the tree.
    :return: Height of the tree in terms of edges.
    """
    root = build_tree_from_level_order(tree)
    return max_height(root) - 1  # Subtract 1 to get the height in terms of edges


# Example usage
tree = [10, 20, 30, 40, 28, 27, 50, 29]
print(find_max_height(tree))  # Output should be 3
