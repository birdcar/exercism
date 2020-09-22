def is_isogram(word):
    """
    Determine if a word or phrase is an isogram.
    """
    try:
        word = [char for char in word.lower() if char.isalpha()]
        
        if len(word) == len(set(word)):
            return True
    except AttributeError:
        print("You need to input a string")
    
    return False

