"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
"""
def sum_mix(arr):
    total = 0
    for i in arr:
        num = int(i)
        total += num
    return total