# Write here the code challenge solution

from collections import deque

class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge from u to v. The graph is undirected
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def bfs(self, start_value):
        """
        Perform Breadth-First Search (BFS) starting from the given node.
        
        :param start_value: The value of the starting node.
        :return: A list of values of nodes visited during BFS.
        """
        if start_value not in self.graph:
            return []

        visited = set()  # To track visited nodes
        queue = deque([start_value])  # Queue to manage the BFS process
        result = []

        while queue:
            # Dequeue a node from the front of the queue
            current_node = queue.popleft()
            
            if current_node not in visited:
                # Mark the node as visited
                visited.add(current_node)
                # Append to the result list
                result.append(current_node)

                # Enqueue all adjacent nodes that haven't been visited yet
                for neighbor in self.graph.get(current_node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result
