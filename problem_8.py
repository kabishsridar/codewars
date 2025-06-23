""" Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
 """
def solution(string):
    result = []
    for char in range(1,len(string) + 1):
        result.append(string[-char])
    return ''.join(result)
