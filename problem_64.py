"""
Design a data structure that supports the following two operations:

addWord / add_word which adds a word,
search which searches a literal word or a regular expression string containing lowercase letters "a-z" or "." where "." can represent any letter. Return true if the search term fully matches any word previously added; otherwise, return false.
You may assume that all given words contain only lowercase letters.

Examples
wd = WordDictionary()

wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")

wd.search("pad") == False
wd.search("bad") == True
wd.search(".ad") == True
wd.search("b..") == True
Note: the data structure will be initialized multiple times during the tests!
"""
class WordDictionary:
    def __init__(self):
        self.lst = []

    def add_word(self, word):
        self.lst.append(word)

    def search(self, word):
        for w in self.lst:
            if len(w) != len(word):
                continue
            match = True
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    match = False
                    break
            if match:
                return True
        return False