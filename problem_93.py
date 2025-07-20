""" Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n). The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. If both letters are the same, order them normally (lexicographically), again, case-insensitive.

Example:

sort_it('bid, zag', 2) #=> 'zag, bid'
The length of all words provided in the list will be >= n. The format will be "x, x, x". In Haskell you'll get a list of Strings instead. """

def sort_it(words, n):
    word_list = words.split(',')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip()

    sort_data = []
    for w in word_list:
        sort_data.append((w[n-1].lower(), w.lower(), w))

    sort_data.sort()

    result = []
    for item in sort_data:
        result.append(item[2])

    return ', '.join(result)