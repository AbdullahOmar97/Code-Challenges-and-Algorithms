import pytest
from queue import Queue
from challenge04 import reverse_queue

def test_reverse_queue():
    """
    Test reversing a queue with multiple elements.
    """
    q = Queue()
    for i in range(5, 0, -1):
        q.put(i)
    
    expected_output = [1, 2, 3, 4, 5]
    reversed_queue = reverse_queue(q)
    
    result = []
    while not reversed_queue.empty():
        result.append(reversed_queue.get())
    
    assert result == expected_output

def test_reverse_queue_single_element():
    """
    Test reversing a queue with a single element.
    """
    q = Queue()
    q.put(1)
    
    expected_output = [1]
    reversed_queue = reverse_queue(q)
    
    result = []
    while not reversed_queue.empty():
        result.append(reversed_queue.get())
    
    assert result == expected_output

def test_reverse_queue_empty():
    """
    Test reversing an empty queue.
    """
    q = Queue()
    
    expected_output = []
    reversed_queue = reverse_queue(q)
    
    result = []
    while not reversed_queue.empty():
        result.append(reversed_queue.get())
    
    assert result == expected_output
