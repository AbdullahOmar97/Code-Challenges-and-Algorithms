# Write your test here
import pytest
from challenge05 import Node, LinkedList, insert_after

def test_insert_after():
    # Create a linked list
    ll = LinkedList()
    for i in range(1, 7):
        ll.append(i)
    
    # Find the node with value 2
    before_node = ll.find(2)
    
    # Create a new node with value 3
    new_node = Node(3)
    
    # Insert new_node after before_node
    insert_after(before_node, new_node)
    
    # Check if the list is [1, 2, 3, 3, 4, 5, 6]
    assert ll.to_list() == [1, 2, 3, 3, 4, 5, 6]
    
    # Additional checks can be added for different positions and edge cases

if __name__ == "__main__":
    pytest.main()
