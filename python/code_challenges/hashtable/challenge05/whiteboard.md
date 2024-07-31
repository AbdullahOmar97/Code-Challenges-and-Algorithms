#### whiteboard.md

## Problem Domain
- **Input**: Two arrays of integers, `arr1` and `arr2`.
- **Output**: An array containing the unique intersection of the two input arrays.

## Test Cases
- **Test Case 1**:
  - Input: `arr1 = [1, 2, 2, 1]`, `arr2 = [2, 2]`
  - Output: `[2]`
- **Test Case 2**:
  - Input: `arr1 = [4, 9, 5]`, `arr2 = [9, 4, 9, 8, 4]`
  - Output: `[4, 9]` or `[9, 4]`
- **Test Case 3**:
  - Input: `arr1 = [1, 3, 4, 6]`, `arr2 = [4, 5, 6, 7]`
  - Output: `[4, 6]` or `[6, 4]`
- **Test Case 4**:
  - Input: `arr1 = [2, 2, 2]`, `arr2 = [2, 2]`
  - Output: `[2]`
- **Test Case 5**:
  - Input: `arr1 = []`, `arr2 = [1, 2, 3]`
  - Output: `[]`
- **Test Case 6**:
  - Input: `arr1 = [1, 2, 3]`, `arr2 = []`
  - Output: `[]`
- **Test Case 7**:
  - Input: `arr1 = []`, `arr2 = []`
  - Output: `[]`
- **Test Case 8**:
  - Input: `arr1 = [1, 2, 3, 4, 5]`, `arr2 = [6, 7, 8, 9, 10]`
  - Output: `[]`
- **Test Case 9**:
  - Input: `arr1 = [1, 2, 3, 4, 5]`, `arr2 = [5, 4, 3, 2, 1]`
  - Output: `[1, 2, 3, 4, 5]` or `[5, 4, 3, 2, 1]` or `[3, 4, 5, 1, 2]` or `[2, 1, 4, 3, 5]`

## Visualization
![alt text](<لقطة شاشة 2024-07-31 080450.png>)

## Algorithm
1. Convert `arr1` to a set called `set1`.
2. Convert `arr2` to a set called `set2`.
3. Compute the intersection of `set1` and `set2`.
4. Convert the resulting set to a list.
5. Return the list.

## Big O
- **Time Complexity:** O(n + m)
  - Converting arrays to sets takes O(n) and O(m) time.
  - Finding the intersection of two sets takes O(min(n, m)) time.
- **Space Complexity:** O(n + m)
  - Storing two sets takes O(n) and O(m) space.

## Step Through
1. Input: `arr1 = [1, 2, 2, 1]`, `arr2 = [2, 2]`
2. Convert `arr1` to set: `set1 = {1, 2}`
3. Convert `arr2` to set: `set2 = {2}`
4. Find intersection: `set1 & set2` → `{2}`
5. Convert to list: `[2]`
6. Return: `[2]`
