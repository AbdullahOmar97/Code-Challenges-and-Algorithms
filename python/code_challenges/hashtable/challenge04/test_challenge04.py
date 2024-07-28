# Write your test here
import pytest
from challenge04 import sort_people

def test_sort_people():
    """
    Tests the sort_people function with multiple test cases to ensure correctness.
    """
    result1 = sort_people(["Alice", "Bob", "Bob"], [155, 185, 150])
    expected1 = ["Bob", "Alice", "Bob"]
    print(f"Test Case 1: Input: (['Alice', 'Bob', 'Bob'], [155, 185, 150]), Expected: {expected1}, Got: {result1}")
    assert result1 == expected1
    
    result2 = sort_people(["John", "Doe", "Jane"], [190, 165, 180])
    expected2 = ["John", "Jane", "Doe"]
    print(f"Test Case 2: Input: (['John', 'Doe', 'Jane'], [190, 165, 180]), Expected: {expected2}, Got: {result2}")
    assert result2 == expected2
    
    result3 = sort_people([], [])
    expected3 = []
    print(f"Test Case 3: Input: ([], []), Expected: {expected3}, Got: {result3}")
    assert result3 == expected3
    
    result4 = sort_people(["Single"], [100])
    expected4 = ["Single"]
    print(f"Test Case 4: Input: (['Single'], [100]), Expected: {expected4}, Got: {result4}")
    assert result4 == expected4
    
    result5 = sort_people(["A", "B", "C"], [160, 160, 160])
    expected5 = ["A", "B", "C"]
    print(f"Test Case 5: Input: (['A', 'B', 'C'], [160, 160, 160]), Expected: {expected5}, Got: {result5}")
    assert result5 == expected5

if __name__ == "__main__":
    test_sort_people()
    print("All tests passed.")
