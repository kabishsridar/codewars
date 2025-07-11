"""
In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

The first element of the array is at index 0.

Good luck!

If you like this Kata, try:"""
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def total(arr):
    total_sum = 0
    for num in range(len(arr)):
        if isprime(num):
            total_sum += arr[num]
    return total_sum