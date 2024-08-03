from challenge01 import Graph

def test_bfs():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'G')
    g.add_edge('F', 'H')
    g.add_edge('F', 'I')
    g.add_edge('G', 'K')

    # Test BFS traversal starting from 'A'
    result = g.bfs('A')
    print(f"BFS starting from 'A': {result}")
    assert result == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']

    # Test BFS traversal starting from 'C'
    result = g.bfs('C')
    print(f"BFS starting from 'C': {result}")
    assert result == ['C', 'A', 'E', 'F', 'B', 'G', 'H', 'I', 'D', 'K']

    # Test BFS traversal starting from 'G'
    result = g.bfs('G')
    print(f"BFS starting from 'G': {result}")
    assert result == ['G', 'E', 'K', 'C', 'A', 'F', 'B', 'H', 'I', 'D']

    # Test BFS traversal starting from a node not connected to any other nodes
    g.add_edge('X', 'Y')
    result = g.bfs('X')
    print(f"BFS starting from 'X': {result}")
    assert result == ['X', 'Y']

if __name__ == '__main__':
    test_bfs()
    print("All tests passed!")
