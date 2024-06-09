from queue import Queue

def reverse_queue(queue):
    """
    Reverse the order of elements in a given queue.

    This function uses a stack to reverse the elements of the queue.
    It first dequeues all elements from the queue and pushes them onto a stack,
    then pops all elements from the stack and enqueues them back to the queue,
    effectively reversing their order.

    Parameters:
    queue (Queue): The queue to be reversed.

    Returns:
    Queue: The reversed queue.
    """
    stack = []
    
    # Dequeue all elements from the queue and push them onto the stack
    while not queue.empty():
        stack.append(queue.get())
    
    # Pop all elements from the stack and enqueue them back to the queue
    while stack:
        queue.put(stack.pop())
    
    return queue
