# Write here the code challenge solution

def find_first_repeated_word(s):
    """
    Function to find the first repeated word in a string.

    Args:
    s (str): The input string.

    Returns:
    str: The first repeated word in uppercase if found, otherwise 'No Repetition'.
    """
    word_set = set()
    words = s.split()
    
    for word in words:
        clean_word = word.strip('.').strip(',').upper()  # Normalize by converting to uppercase
        if clean_word in word_set:
            return clean_word
        word_set.add(clean_word)
    
    return 'No Repetition'
