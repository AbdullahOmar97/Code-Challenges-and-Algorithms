import pytest
from challenge05 import Node, LinkedList, insert_after

def test_insert_after():
    # Create a linked list
    ll = LinkedList()
    for i in range(1, 7):
        ll.append(i)
    
    # Print initial state of the linked list
    print("Initial Linked List:")
    print(ll.to_list())
    
    # Find the node with value 2
    before_node = ll.find(2)
    print("\nFound node with value 2:")
    print(before_node.value)
    
    # Create a new node with value 3
    new_node = Node(3)
    print("\nCreating new node with value 3.")
    
    # Insert new_node after before_node
    insert_after(before_node, new_node)
    print("\nInserted node with value 3 after node with value 2.")
    
    # Print the current state of the linked list
    print("\nUpdated Linked List:")
    print(ll.to_list())
    
    # Check if the list is [1, 2, 3, 3, 4, 5, 6]
    assert ll.to_list() == [1, 2, 3, 3, 4, 5, 6]
    
    # Additional checks can be added for different positions and edge cases
    # Example: Inserting at the beginning
    new_node_beginning = Node(0)
    insert_after(ll.head, new_node_beginning)
    print("\nInserted node with value 0 at the beginning.")
    print("\nLinked List after inserting node with value 0 at the beginning:")
    print(ll.to_list())
    assert ll.to_list() == [1, 0, 2, 3, 3, 4, 5, 6]
    
    # Example: Inserting at the end
    new_node_end = Node(7)
    insert_after(ll.find(6), new_node_end)
    print("\nInserted node with value 7 at the end.")
    print("\nLinked List after inserting node with value 7 at the end:")
    print(ll.to_list())
    assert ll.to_list() == [1, 0, 2, 3, 3, 4, 5, 6, 7]
    
    # Example: Inserting in the middle with different value
    new_node_middle = Node(4)
    insert_after(ll.find(3), new_node_middle)
    print("\nInserted node with value 4 after node with value 3.")
    print("\nLinked List after inserting node with value 4 after node with value 3:")
    print(ll.to_list())
    assert ll.to_list() == [1, 0, 2, 3, 4, 3, 4, 5, 6, 7]

    # Example: Inserting after None should raise ValueError
    print("\nTesting inserting after None (should raise ValueError).")
    with pytest.raises(ValueError):
        insert_after(None, Node(999))

if __name__ == "__main__":
    pytest.main()
