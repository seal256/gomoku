import pickle

class player(object):
    """Random gomoku player"""
    def __init__(self, fname = './data/state_val_3x3.pkl'):
        self.state_val = pickle.load(open(fname, 'rb'))        

    def get_move(self, game):
        best_val = -10.
        best_move = None
        for move in game.get_valid_moves():
            game.check_move(move)
            state = game.get_state_hash()
            if not self.state_val.has_key(state):
                print('Error: Absent state')
                print(game.game_state)
                game.delete_move()
                continue

            val = self.state_val[state]    
            if val > best_val:
                best_val = val
                best_move = move
            game.delete_move()

        print('Best move:', best_move, best_val)
        return best_move