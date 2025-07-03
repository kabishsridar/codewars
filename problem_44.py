"""
Task
Create a class that imitates a select screen. The cursor can move to left or right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the methods to_the_right and to_the_left which moves the cursor.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])

menu.display() ➞ "[[1], 2, 3]"

menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"

menu.to_the_left()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_left()
menu.display() ➞ "[1, [2], 3]"
Notes
The cursor should wrap back round to the start once it reaches the end.
"""
class Menu:
    def __init__(self, menu):
        self.menu = menu
        self.index = 0
    
    def to_the_right(self):
        if self.index == len(self.menu) - 1:
            self.index = 0
        else:
            self.index += 1
        
    def to_the_left(self):
        if self.index == 0:
            self.index = len(self.menu) - 1
        else:
            self.index -= 1
        
    def display(self):
        result = []
        for i in range(len(self.menu)):
            item_str = str(self.menu[i])
            if i == self.index:
                result.append([item_str])
            else:
                result.append(item_str)
        return f"{result}"