# Whiteboard

## Problem Domain
- **Input**:
  - A directed graph represented as a list of edges. Each edge is a pair of vertices `[u, v]` indicating a directed edge from vertex `u` to vertex `v`.
- **Output**:
  - A boolean value indicating whether the graph is strongly connected. A graph is strongly connected if there is a path between any pair of vertices in both directions.

## Test Cases
- **Test Case 1**:
  - **Input**: `[[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]`
  - **Output**: `False`
  - **Explanation**: The graph is not strongly connected because there is no path from vertex 7 to vertices 4, 5, or 6.
- **Test Case 2**:
  - **Input**: `[[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]`
  - **Output**: `True`
  - **Explanation**: The graph is strongly connected as there is a path between any pair of vertices.
- **Test Case 3**:
  - **Input**: `[[0, 1], [1, 2], [2, 0], [3, 4]]`
  - **Output**: `False`
  - **Explanation**: The graph is not strongly connected because vertices 3 and 4 are disconnected from the rest of the graph.

## Visualization
- **Graph Representation**:
  - **Test Case 1**:
![alt text](<graphviz (2).png>)
    Not all vertices are reachable from every other vertex.
  
  - **Test Case 2**:
![alt text](<graphviz (3).png>)
    All vertices are reachable from every other vertex.
  
  - **Test Case 3**:
![alt text](<graphviz (4).png>)
    Vertices 3 and 4 are disconnected from the main cycle.

## Algorithm
1. **Perform DFS** from any vertex to check if all vertices are reachable.
   - If all vertices are not visited, return `False`.
2. **Transpose the graph** (reverse the direction of all edges).
3. **Perform DFS again** on the transposed graph.
   - If all vertices are not visited in this second DFS, return `False`.
4. If both DFS traversals visit all vertices, return `True`.

## Big O
- **Time Complexity**: `O(V + E)`
  - Where `V` is the number of vertices and `E` is the number of edges. The algorithm involves performing DFS twice, which is linear in terms of the number of vertices and edges.
- **Space Complexity**: `O(V)`
  - We use space to store the visited array and the adjacency list for the graph.

## Step Through
- **Step 1**: Start DFS from vertex 0.
  - Mark vertex 0 as visited, then visit all its neighbors.
  - Continue the DFS until all reachable vertices are visited.
- **Step 2**: Check if all vertices are visited.
  - If any vertex is not visited, the graph is not strongly connected.
- **Step 3**: Transpose the graph.
  - Reverse the direction of all edges in the graph.
- **Step 4**: Start DFS from the same vertex on the transposed graph.
  - Mark the vertex as visited, then visit all its neighbors.
- **Step 5**: Check if all vertices are visited.
  - If any vertex is not visited, the graph is not strongly connected.
- **Step 6**: If all vertices are visited in both DFS traversals, the graph is strongly connected.
