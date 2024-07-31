# Write here the code challenge solution

def intersection(arr1, arr2):
    """
    Function to find the intersection of two arrays.
    
    Parameters:
    arr1 (list): First list of integers.
    arr2 (list): Second list of integers.
    
    Returns:
    list: A list containing the unique intersection of the two input lists.
    """
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)
