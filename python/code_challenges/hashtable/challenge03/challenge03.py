# Write here the code challenge solution

def sum_of_unique_elements(nums):
    """
    Calculate the sum of unique elements in the array.

    Unique elements are those that appear exactly once in the array.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The summation of unique elements in the list.
    """
    from collections import Counter

    # Count the occurrences of each element in the list
    counts = Counter(nums)

    # Calculate the sum of elements that appear exactly once
    unique_sum = sum(key for key, value in counts.items() if value == 1)

    return unique_sum
