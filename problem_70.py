from sympy import *
def total(arr):
    total_sum = 0
    for num in range(len(arr)):
        if isprime(num):
            total_sum += arr[num]
    return total_sum
total([1,4,2,5,3,56,3,56,3,3,42,34,33,4])