"""
Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.

snoopy.bark() #return "Woof"
scoobydoo.bark() #undefined
Use method prototypes to enable all Dogs to bark.

"""
class Dog (): # create a class Dog
  def __init__(self, breed): # constructor or init method
    self.breed = breed
    

snoopy = Dog("Beagle") # set snoopy to an object

snoopy.bark = lambda: "Woof" # sets the bark method woof

scoobydoo = Dog("Great Dane")

scoobydoo.bark = lambda: "Woof"