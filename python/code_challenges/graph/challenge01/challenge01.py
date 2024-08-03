# Write here the code challenge solution

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
        # Assuming it's an undirected graph, add the reverse edge
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[neighbor].append(node)

    def bfs(self, start_value):
        """
        Perform BFS traversal starting from start_value.

        :param start_value: The starting node value for BFS
        :return: A list of visited nodes in BFS order
        """
        visited = set()
        queue = [start_value]
        bfs_order = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                bfs_order.append(current)
                for neighbor in self.graph.get(current, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return bfs_order
