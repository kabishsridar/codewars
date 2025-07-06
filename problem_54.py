"""
This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version.

Task:
Find out "B"(Bug) in a lot of "A"(Apple).

There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

input: string Array apple

output: Location of "B", [x,y]

sample_test_cases = [
    #        apple                expected

    ([['B','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A']],      (0, 0)
    ),

    ([['A','A','A','A','A'],
      ['A','B','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A']],      (1, 1)
    ),  

    ([['A','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','A','A','A','A'],
      ['A','B','A','A','A']],      (4, 1)
    ),
]
"""
def sc(apple):
    for i in range(len(apple)):
        for j in range(len(apple[i])):
            if apple[i][j] == 'B':
                return (i, j)