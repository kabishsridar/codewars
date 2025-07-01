"""
Imagine you are creating a game where the user has to guess the correct number. But there is a limit of how many guesses the user can do.

If the user tries to guess more than the limit, the function should throw an error.
If the user guess is right it should return true.
If the user guess is wrong it should return false and lose a life.
Can you finish the game so all the rules are met?
"""
class Guesser: # creating a class
    def __init__(self, number, lives): # a constructor or a init method
        self.number = number
        self.lives = lives # set values
  
    def guess(self,n):
        if self.lives == 0: # raises the error when the lives  completed
            raise Exception("Omae wa mo shindeiru")
        if n == self.number: # if number is guessed correctly
            return True
        elif n != self.number: # if number doesn' matches
            self.lives -= 1
            return False
