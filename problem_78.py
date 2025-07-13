"""Write a function revSub which reverses all sublists where consecutive elements are even. Note that the odd numbers should remain where they are.

Example
With [1,2,4,5,9] as input, we should get [1,4,2,5,9]. Here, because [2,4] is a sublist of consecutive even numbers, it should be flipped. There could be more than one sublist of even numbers, or none at all.

A few other examples:

[] -> []
[2,4] -> [4,2]
[2,4,3] -> [4,2,3]
[2,4,3,10,2] -> [4,2,3,2,10]
Have fun coding!
"""
def rev_sub(arr):
    result = []
    even_num = []
    
    for num in arr:
        if num % 2 == 0:
            even_num.append(num)
        else:
            if even_num:
                result.extend(even_num[::-1])
                even_num = []
            result.append(num)
    if even_num:
        result.extend(even_num[::-1])
    return result