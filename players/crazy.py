from random import randint, seed

class player(object):
    """Random gomoku player"""
    def __init__(self):
        pass
        #seed(1828)

    def get_move(self, game):
        available = game.get_valid_moves()

        if len(available) == 0:
            return None
        
        n = randint(0, len(available) - 1)
        return available[n]


