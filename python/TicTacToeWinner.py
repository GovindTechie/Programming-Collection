class Solution(object):
    def tictactoe(self, moves):
        winnerProb = [[(0,0),(0,1),(0,2)],
                      [(1,0),(1,1),(1,2)],
                      [(2,0),(2,1),(2,2)],
                      [(0,0),(1,0),(2,0)],
                      [(0,1),(1,1),(2,1)],
                      [(0,2),(1,2),(2,2)],
                      [(0,0),(1,1),(2,2)],
                      [(0,2),(1,1),(2,0)] 
                      ]
        
        a_moves = moves[::2]
        b_moves = moves[1::2]
        a_set = set(tuple(move) for move in a_moves)
        b_set = set(tuple(move) for move in b_moves)

        if any(set(win).issubset(a_set) for win in winnerProb):
            return "A Wins"
        elif any(set(win).issubset(b_set) for win in winnerProb):
            return "B Wins"
        elif len(moves) < 9:
            return "Pending"
        else:
            return "Draw"


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
s1 = Solution()
print(f"The moves are (A plays first): {moves}")
print(f"The output of game : {s1.tictactoe(moves)}")