# Write your test here
import pytest
from challenge03 import sum_of_unique_elements

def test_sum_of_unique_elements():
    test_cases = [
        ([1, 2, 3, 2], 4),
        ([1, 2, 3, 4, 5], 15),
        ([1, 1, 1, 1, 1], 0),
        ([], 0),
        ([1, 2, 2, 3, 3, 4, 5], 10),
        ([7, 7, 8, 9, 9, 10], 18),
        ([0, 0, 0, 0, 1], 1),
        ([-1, -2, -2, -3, -4, -4], -4)
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = sum_of_unique_elements(nums)
        print(f"Test case {i}: Input({nums}) -> Expected({expected}), Result({result})")
        assert result == expected, f"Test case {i} failed"

if __name__ == "__main__":
    test_sum_of_unique_elements()
