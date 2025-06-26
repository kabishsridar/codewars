"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""
def find_short(s):
    length = []
    for word in s.split():
        length.append(len(word))
        
    minimum = min(length)
    return minimum # l: shortest word length