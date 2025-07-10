"""
Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].

"""
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, text):
        result = ''
        for char in text:
            upper_char = char.upper()
            if upper_char in self.alphabet:
                index = self.alphabet.index(upper_char)
                shifted_index = (index + self.shift) % 26
                result += self.alphabet[shifted_index]
            else:
                result += char
        return result

    def decode(self, text):
        result = ''
        for char in text:
            upper_char = char.upper()
            if upper_char in self.alphabet:
                index = self.alphabet.index(upper_char)
                shifted_index = (index - self.shift) % 26
                result += self.alphabet[shifted_index]
            else:
                result += char
        return result
