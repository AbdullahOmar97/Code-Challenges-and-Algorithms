# Write your test here'
# test_challenge01.py

import pytest
from challenge01 import MyQueue

def test_queue_operations():
    myQueue = MyQueue()
    assert myQueue.empty() == True

    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1  # return 1
    assert myQueue.pop() == 1   # return 1
    assert myQueue.empty() == False  # return False

    myQueue.push(3)
    assert myQueue.peek() == 2  # return 2
    assert myQueue.pop() == 2   # return 2
    assert myQueue.pop() == 3   # return 3
    assert myQueue.empty() == True  # return True

if __name__ == "__main__":
    pytest.main()
