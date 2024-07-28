# Write here the code challenge solution

def sort_people(names, heights):
    """
    Reorders and returns the list of names based on the corresponding heights in descending order.

    Args:
    names (list of str): List of people's names.
    heights (list of int): List of people's heights corresponding to the names.

    Returns:
    list of str: List of names reordered by descending heights.
    """
    # Combine names and heights into a list of tuples
    people_with_heights = list(zip(names, heights))
    
    # Sort the list of tuples by height in descending order
    people_with_heights.sort(key=lambda x: x[1], reverse=True)
    
    # Extract the names from the sorted list
    sorted_names = [person[0] for person in people_with_heights]
    
    return sorted_names
