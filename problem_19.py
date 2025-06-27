"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

"""
def remove_exclamation_marks(s):
    string = ""
    for i in s:
        if i == "!":
            i = ""
        else:
            string += i
    return string
        