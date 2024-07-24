# whiteboard.md

## Problem Domain

- **Input**: A list of integers (`nums`), where each integer can be positive, negative, or zero.
- **Output**: An integer representing the sum of unique elements in the list. Unique elements are those that appear exactly once.

## Test Cases

1. **Test Case 1**:
   - **Input**: `[1, 2, 3, 2]`
   - **Output**: `4`
   - **Explanation**: The unique elements are `1` and `3`, and their sum is `4`.

2. **Test Case 2**:
   - **Input**: `[1, 2, 3, 4, 5]`
   - **Output**: `15`
   - **Explanation**: All elements are unique, so the sum is the sum of all elements.

3. **Test Case 3**:
   - **Input**: `[1, 1, 1, 1, 1]`
   - **Output**: `0`
   - **Explanation**: There are no unique elements, so the sum is `0`.

4. **Test Case 4**:
   - **Input**: `[]`
   - **Output**: `0`
   - **Explanation**: An empty list has no unique elements, so the sum is `0`.

5. **Test Case 5**:
   - **Input**: `[1, 2, 2, 3, 3, 4, 5]`
   - **Output**: `10`
   - **Explanation**: The unique elements are `1`, `4`, and `5`, and their sum is `10`.

6. **Test Case 6**:
   - **Input**: `[7, 7, 8, 9, 9, 10]`
   - **Output**: `18`
   - **Explanation**: The unique elements are `8` and `10`, and their sum is `18`.

7. **Test Case 7**:
   - **Input**: `[0, 0, 0, 0, 1]`
   - **Output**: `1`
   - **Explanation**: The unique element is `1`, and its sum is `1`.

8. **Test Case 8**:
   - **Input**: `[-1, -2, -2, -3, -4, -4]`
   - **Output**: `-4`
   - **Explanation**: The unique element is `-3`, and its sum is `-3`.

## Visualization


[text](whiteboard.md)


## Algorithm

1. **Count Occurrences**: Use a counter to count the number of occurrences of each element in the list.
2. **Filter Unique Elements**: Identify elements that appear exactly once.
3. **Sum Unique Elements**: Compute the sum of these unique elements.
4. **Return Result**: Return the computed sum.

## Big O

- **Time Complexity**: `O(n)`
  - Counting the occurrences takes linear time.
  - Summing the unique elements takes linear time relative to the number of unique elements.
  
- **Space Complexity**: `O(n)`
  - Space is used for storing the counts of elements.

## Step Through

1. **Input**: `[1, 2, 2, 3, 3, 4, 5]`
2. **Count Occurrences**: `{1: 1, 2: 2, 3: 2, 4: 1, 5: 1}`
3. **Identify Unique Elements**: `1`, `4`, `5`
4. **Compute Sum**: `1 + 4 + 5 = 10`
5. **Output**: `10`
