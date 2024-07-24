# Write here the code challenge solution

import string

def find_first_repeated_word(s):
    """
    Function to find the first repeated word in a string.

    Args:
    s (str): The input string.

    Returns:
    str: The first repeated word in uppercase if found, otherwise 'No Repetition'.
    """
    word_set = set()
    
    # Translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Split the string into words
    words = s.split()
    
    for word in words:
        # Normalize by converting to uppercase and removing punctuation
        clean_word = word.translate(translator).upper().strip()
        
        if clean_word in word_set:
            return clean_word
        
        word_set.add(clean_word)
    
    return 'No Repetition'
