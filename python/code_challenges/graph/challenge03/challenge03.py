# Write here the code challenge solution
# challenge03.py

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with a specified number of vertices.
        :param vertices: Number of vertices in the graph
        """
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Default dictionary to store the graph

    def add_edge(self, u, v):
        """
        Adds a directed edge from vertex u to vertex v.
        :param u: The starting vertex
        :param v: The ending vertex
        """
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        """
        A utility function to perform DFS starting from vertex v.
        :param v: The starting vertex
        :param visited: A list to keep track of visited vertices
        """
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def get_transpose(self):
        """
        Function that returns the transpose of the graph (reverse all edges).
        :return: Transposed graph
        """
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def is_strongly_connected(self):
        """
        Checks if the graph is strongly connected.
        :return: True if strongly connected, False otherwise
        """
        # Step 1: Perform DFS from the first vertex
        visited = [False] * self.V
        self.dfs_util(0, visited)

        # If DFS traversal doesn't visit all vertices, then return False
        if any(not i for i in visited):
            return False

        # Step 2: Get the transpose of the graph
        gr = self.get_transpose()

        # Step 3: Perform DFS on the transposed graph
        visited = [False] * self.V
        gr.dfs_util(0, visited)

        # If all vertices are visited in the second DFS, then the graph is strongly connected
        return not any(not i for i in visited)
