# test_challenge04.py

from challenge04 import ListNode, reverseLinkedList, createLinkedList, printLinkedList

def test_reverseLinkedList():
    # Test case 1
    head = createLinkedList([1, 2, 3, 4, 5])
    reversed_head = reverseLinkedList(head)
    assert printLinkedList(reversed_head) == [5, 4, 3, 2, 1], "Test case 1 failed"

    # Test case 2
    head = createLinkedList([1])
    reversed_head = reverseLinkedList(head)
    assert printLinkedList(reversed_head) == [1], "Test case 2 failed"

    # Test case 3
    head = createLinkedList([])
    reversed_head = reverseLinkedList(head)
    assert printLinkedList(reversed_head) == [], "Test case 3 failed"

    # Test case 4
    head = createLinkedList([1, 2])
    reversed_head = reverseLinkedList(head)
    assert printLinkedList(reversed_head) == [2, 1], "Test case 4 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_reverseLinkedList()
