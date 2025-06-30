def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
