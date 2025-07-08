"""
Your vectors should handle vector additon with an .add() method that takes a second vector as an argument and returns a new vector equal to the sum of the vector you call .add() on and the vector you pass in.

For example:

>>> a = Vector(3, 4)
>>> a.x
3
>>> a.y
4
>>> b = Vector(1, 2)
>>> c = a.add(b)
>>> c.x
4
>>> c.y
6
Adding vectors when you have their components is easy: just add the two x components together and the two y components together to get the x and y components for the vector sum.
"""
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, b):
        return Vector(self.x + b.x, self.y + b.y)