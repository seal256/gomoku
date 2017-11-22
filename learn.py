import pickle
from game import LineGame
from learning.game_tree import FullGameTree

def game_tree_3x3():
    game = LineGame(3,3)
    start_state = game.get_state_hash()
    tree = FullGameTree()
    tree.dfs(game)
    pickle.dump(tree.state_val, open('data/state_val_3x3.pkl', 'wb'))
    print(len(tree.state_val))
    print(start_state, tree.state_val[start_state])

if __name__ == '__main__':
    game_tree_3x3()