import pytest
from challenge01 import MyQueue

def test_queue_operations():
    myQueue = MyQueue()
    assert myQueue.empty() == True
    print("Initial empty check:", myQueue.empty())

    myQueue.push(1)
    myQueue.push(2)
    print("After pushing 1 and 2:")
    print("Peek:", myQueue.peek())  # should return 1
    assert myQueue.peek() == 1

    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 1
    assert popped_value == 1
    print("Empty check after one pop:", myQueue.empty())
    assert myQueue.empty() == False

    myQueue.push(3)
    print("After pushing 3:")
    print("Peek:", myQueue.peek())  # should return 2
    assert myQueue.peek() == 2

    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 2
    assert popped_value == 2

    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 3
    assert popped_value == 3

    print("Final empty check:", myQueue.empty())
    assert myQueue.empty() == True

def test_additional_operations():
    myQueue = MyQueue()
    myQueue.push(4)
    myQueue.push(5)
    print("After pushing 4 and 5:")
    print("Peek:", myQueue.peek())  # should return 4
    assert myQueue.peek() == 4

    myQueue.push(6)
    print("After pushing 6:")
    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 4
    assert popped_value == 4

    print("Peek after popping 4:", myQueue.peek())  # should return 5
    assert myQueue.peek() == 5

    myQueue.push(7)
    print("After pushing 7:")
    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 5
    assert popped_value == 5

    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 6
    assert popped_value == 6

    popped_value = myQueue.pop()
    print("Pop:", popped_value)  # should return 7
    assert popped_value == 7

    print("Final empty check:", myQueue.empty())
    assert myQueue.empty() == True

if __name__ == "__main__":
    pytest.main()
