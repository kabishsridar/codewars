"""
A keyword cipher is a monoalphabetic cipher which uses a "keyword" to provide encryption. It is somewhat similar to a Caesar cipher.

In a keyword cipher, repeats of letters in the keyword are removed and the alphabet is reordered such that the letters in the keyword appear first, followed by the rest of the letters in the alphabet in their otherwise usual order.

E.g. for an uppercase latin alphabet with keyword of "KEYWORD":

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

becomes:

K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

such that:

cipher.encode('ABCHIJ') == 'KEYABC'
cipher.decode('KEYABC') == 'ABCHIJ'
All letters in the keyword will also be in the alphabet. For the purpose of this kata, only the first occurence of a letter in a keyword should be used. Any characters not provided in the alphabet should be left in situ when encoding or decoding.


"""
class keyword_cipher(object):
    
    def __init__(self, abc, keyword):
        self.abc = abc
        
        seen = set()
        cipher_list = []
        for ch in keyword:
            if ch not in seen:
                seen.add(ch)
                cipher_list.append(ch)
        for ch in abc:
            if ch not in seen:
                cipher_list.append(ch)
        
        self.cipher = "".join(cipher_list)
        
        self.encode_mapping = {}
        for i in range(len(abc)):
            self.encode_mapping[abc[i]] = self.cipher[i]
        
        self.decode_mapping = {}
        for i in range(len(abc)):
            self.decode_mapping[self.cipher[i]] = abc[i]
    
    def encode(self, plain):
        result = []
        for ch in plain:
            if ch in self.encode_mapping:
                result.append(self.encode_mapping[ch])
            else:
                result.append(ch)
        return "".join(result)
    
    def decode(self, ciphered):
        result = []
        for ch in ciphered:
            if ch in self.decode_mapping:
                result.append(self.decode_mapping[ch])
            else:
                result.append(ch)
        return "".join(result)