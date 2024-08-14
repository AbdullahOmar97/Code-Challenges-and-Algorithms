# Write your test here
# test_challenge03.py

import pytest
from challenge03 import Graph

def test_strongly_connected():
    g1 = Graph(7)
    edges1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
    for u, v in edges1:
        g1.add_edge(u-1, v-1)  # Subtracting 1 for 0-based indexing
    result1 = g1.is_strongly_connected()
    print(f"Test case 1: {result1}")  # Print the result
    assert result1 == False, "Test case 1 failed"

    g2 = Graph(5)
    edges2 = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
    for u, v in edges2:
        g2.add_edge(u-1, v-1)  # Subtracting 1 for 0-based indexing
    result2 = g2.is_strongly_connected()
    print(f"Test case 2: {result2}")  # Print the result
    assert result2 == True, "Test case 2 failed"

if __name__ == "__main__":
    pytest.main()
