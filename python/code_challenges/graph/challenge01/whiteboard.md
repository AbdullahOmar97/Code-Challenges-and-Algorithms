#### whiteboard.md
## Problem Domain
Implement a graph class with a method that performs a Breadth-First Search (BFS) traversal starting from a given node value. The BFS method should return an array containing the values of the visited nodes in the order they were visited.

- **Input**: 
  - A starting node value from which the BFS traversal begins.
- **Output**: 
  - An array of node values visited in BFS order.

## Test Cases
1. **Graph Structure**:
    - **Input**: `A`
    - **Output**: `["A", "B", "C", "D", "E", "F"]`
    
2. **Graph Structure**:
    - **Input**: `C`
    - **Output**: `["C", "A", "D", "E", "B", "F"]`
    
3. **Graph Structure with Disconnected Node**:
    - **Input**: `X`
    - **Output**: `["X", "Y"]`
    
4. **Single Node Graph**:
    - **Input**: `Z`
    - **Output**: `["Z"]`

## Visualization

![alt text](<لقطة شاشة 2024-08-03 111734.png>)

## Algorithm
1. Initialize an empty set `visited` to keep track of visited nodes.
2. Initialize a queue with the starting node.
3. Initialize an empty list `bfs_order` to store the BFS traversal order.
4. While the queue is not empty:
    - Dequeue a node `current` from the front of the queue.
    - If `current` has not been visited:
        - Mark `current` as visited.
        - Append `current` to `bfs_order`.
        - Enqueue all unvisited neighbors of `current`.
5. Return `bfs_order`.

## Big O
- **Time Complexity**: 
  - O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. Each node and edge is processed once.
- **Space Complexity**: 
  - O(V), where V is the number of vertices. The queue and visited set can grow up to the number of vertices in the graph.

## Step Through
1. **Initialization**:
    - `visited` = {}
    - `queue` = [start_value]
    - `bfs_order` = []
2. **First Iteration**:
    - Dequeue `A`, mark as visited.
    - Append `A` to `bfs_order`: `bfs_order` = ["A"]
    - Enqueue unvisited neighbors: `B`, `C`
    - `queue` = [B, C]
3. **Second Iteration**:
    - Dequeue `B`, mark as visited.
    - Append `B` to `bfs_order`: `bfs_order` = ["A", "B"]
    - Enqueue unvisited neighbors: `D`
    - `queue` = [C, D]
4. **Third Iteration**:
    - Dequeue `C`, mark as visited.
    - Append `C` to `bfs_order`: `bfs_order` = ["A", "B", "C"]
    - Enqueue unvisited neighbors: `E`
    - `queue` = [D, E]
5. **Subsequent Iterations**:
    - Continue until `queue` is empty, visiting nodes in BFS order and enqueuing their unvisited neighbors.
    - Final `bfs_order`: `["A", "B", "C", "D", "E", "F"]`
