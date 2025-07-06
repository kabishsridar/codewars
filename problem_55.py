"""
A triangle is called an equable triangle if its area equals its perimeter. Return true, if it is an equable triangle, else return false. You will be provided with the length of sides of the triangle. Happy Coding!
"""
def equable_triangle(a,b,c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * ( s -a) * (s-b) * (s-c)) ** 0.5
    
    return area == perimeter