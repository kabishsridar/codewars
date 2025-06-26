"""
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""
def rps(p1, p2):
    sc = "scissors"
    pp = "paper"
    rk = "rock"
    if p1 == p2:
        return "Draw!"
    if p1 == sc:
        if p2 == rk:
            return "Player 2 won!"
        elif p2 == pp:
            return "Player 1 won!"
    elif p1 == rk:
        if p2 == sc:
            return "Player 1 won!"
        elif p2 == pp:
            return "Player 2 won"
    elif p1 == pp:
        if p2 == rk:
            return "Player 1 won!"
        elif p2 == sc:
            return "Player 2 won!"