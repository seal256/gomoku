from random import randint, seed

class player(object):
    """Random gomoku player"""
    def __init__(self):
        pass
        #seed(1828)

    def get_move(self, game):
        available = []
        for x in range(game.board_size):
            for y in range(game.board_size):
                if game.board[x][y] is None:
                    available.append((x, y))

        if len(available) == 0:
            return None
        
        n = randint(0, len(available) - 1)
        return available[n]


