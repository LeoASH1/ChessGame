#stores information about current state of chess game
#determines valid moves at given state, keeping track of moves made
class GameState():
    def __init__(self):
        self.board = [
        #can use numpy arrays for IMPROVEMENT
        # using -- instead of 0 for empty space as we can treat it the exact same way as other strings for ease of use
        #2D board where first character is colour and second is piece name
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
