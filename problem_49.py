"""
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"
   
cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"
If a character provided is not in the opposing alphabet, simply leave it as be.
"""
class Cipher:
    def __init__(self, map1, map2):
        self.encode_dict = {}
        self.decode_dict = {}
        
        for i in range(len(map1)):
            c1 = map1[i]
            c2 = map2[i]
            self.encode_dict[c1] = c2
            self.decode_dict[c2] = c1

    def encode(self, s):
        result = []
        for char in s:
            if char in self.encode_dict:
                result.append(self.encode_dict[char])
            else:
                result.append(char)
        return ''.join(result)

    def decode(self, s):
        result = []
        for char in s:
            if char in self.decode_dict:
                result.append(self.decode_dict[char])
            else:
                result.append(char)
        return ''.join(result)
