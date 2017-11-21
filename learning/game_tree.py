

class GameTreeNode:
    def __init__(self, parent_node, state):
        self.state = state # full game state
        self.value = 0. # value of node


class FullGameTree:
    def __init__(self):
        self.nodes = []
    
    def create_tree(self, game):
        game.clean()
        start_state = game.get_current_state()
        self.nodes.append(GameTreeNode(None, None))
        for move in game.get_valid_moves():

    def 
        
