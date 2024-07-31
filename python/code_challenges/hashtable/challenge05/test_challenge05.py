# Write your test here

import pytest
from challenge05 import intersection

def test_intersection():
    result = intersection([1, 2, 2, 1], [2, 2])
    print("Test Case 1 - Expected: [2], Got:", result)
    assert result == [2]

    result = intersection([4, 9, 5], [9, 4, 9, 8, 4])
    print("Test Case 2 - Expected: [4, 9] or [9, 4], Got:", result)
    assert result == [4, 9] or result == [9, 4]

    result = intersection([1, 3, 4, 6], [4, 5, 6, 7])
    print("Test Case 3 - Expected: [4, 6] or [6, 4], Got:", result)
    assert result == [4, 6] or result == [6, 4]

    result = intersection([2, 2, 2], [2, 2])
    print("Test Case 4 - Expected: [2], Got:", result)
    assert result == [2]

    result = intersection([], [1, 2, 3])
    print("Test Case 5 - Expected: [], Got:", result)
    assert result == []

    result = intersection([1, 2, 3], [])
    print("Test Case 6 - Expected: [], Got:", result)
    assert result == []

    result = intersection([], [])
    print("Test Case 7 - Expected: [], Got:", result)
    assert result == []

    result = intersection([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    print("Test Case 8 - Expected: [], Got:", result)
    assert result == []

    result = intersection([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    print("Test Case 9 - Expected: [1, 2, 3, 4, 5] or [5, 4, 3, 2, 1] or [3, 4, 5, 1, 2] or [2, 1, 4, 3, 5], Got:", result)
    assert result == [1, 2, 3, 4, 5] or result == [5, 4, 3, 2, 1] or result == [3, 4, 5, 1, 2] or result == [2, 1, 4, 3, 5]

if __name__ == "__main__":
    test_intersection()
