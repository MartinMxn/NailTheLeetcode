class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0] * 3
        col = [0] * 3
        dia1, dia2 = 0, 0
        turn = 'A'
        for x, y in moves:
            add_on = 1 if turn == 'A' else -1
            row[x] += add_on
            col[y] += add_on
            if x == y: dia1 += add_on
            if x == 2 - y: dia2 += add_on
            
            if abs(row[x]) == 3 or abs(col[y]) == 3: 
                return turn
            if abs(dia1) == 3 or abs(dia2) == 3: 
                return turn
            
            turn = 'B' if turn == 'A' else 'A'
        
        if len(moves) == 9: return 'Draw'
        return 'Pending'
