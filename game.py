import numpy as np


class Amazon(object):
    
    def __init__(self):
        N = 8
        self.board = np.zeros((N, N))	# 0 for blank, 3 for block
        pos1 = [[0, 2], [2, 0], [5, 0], [7, 2]]
        pos2 = [[0, 5], [2, 7], [5, 7], [7, 5]]
        for pos in pos1:
            self.board[pos[0]][pos[1]] = 1
        for pos in pos2:
            self.board[pos[0]][pos[1]] = 2
        self.player = 0
        self.showboard = np.zeros((N, N), dtype=np.object)

    def draw(self):
        dic = { 0: ' ', 1: 'X', 2: 'O', 3: '*' }
        for i in range(8):
            for j in range(8):
                self.showboard[i][j] = dic[self.board[i][j]]
        print(self.showboard)
