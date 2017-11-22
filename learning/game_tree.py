from __future__ import print_function

#class GameTreeNode:
#    def __init__(self, state):
#        self.state = state # full game state
#        self.value = 0. # value of node


class FullGameTree:
    def __init__(self):
        self.state_val = {}
    
    #def create_tree(self, game):
    #    game.clean()
    #    self.dfs(game)
        
    def dfs(self, game): 
        """Depth first search. Values are calculated for first (black) player"""

        if len(self.state_val) % 1000 == 0:
            print('\r', len(self.state_val), end='')

        curr_state = game.get_state_hash()
        if self.state_val.has_key(curr_state): # already seen this state
            return self.state_val[curr_state]

        result = game.check_win()

        if result is True: # current player wins
            value = 1. # black wins
            if game.current_player() == 1: # white wins
                value = -value
            self.state_val[curr_state] = value
            #print(game.game_state)
            return value
        
        if result is None: # draw
            value = 0.
            self.state_val[curr_state] = value
            return value

        # game continues
        values = []
        for move in game.get_valid_moves():
            if not game.check_move(move): # invalid move (this should never happen)
                continue
            values.append(self.dfs(game))
            game.delete_move() # return to previous state

        min_node = game.current_player() == 0 # we explored white moves => we are in min node of minimax tree
        value = 0.
        if min_node:
            value = min(values)
        else:
            value = max(values)
        self.state_val[curr_state] = value
        return value


        
