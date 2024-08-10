# Write your test here

from challenge02 import Graph

def test_bfs():
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'G')
    graph.add_edge('F', 'H')
    graph.add_edge('G', 'I')
    graph.add_edge('H', 'K')

    # Test BFS traversal from 'A'
    result = graph.bfs('A')
    print(f"BFS starting from 'A': {result}")
    expected_output = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']
    assert result == expected_output

    # Test BFS with a different start node
    result = graph.bfs('C')
    print(f"BFS starting from 'C': {result}")
    expected_output = ['C', 'A', 'E', 'F', 'B', 'G', 'H', 'D', 'I', 'K']
    assert result == expected_output

    # Test with node that doesn't exist
    result = graph.bfs('Z')
    print(f"BFS starting from 'Z' (non-existent node): {result}")
    assert result == []

if __name__ == "__main__":
    test_bfs()
