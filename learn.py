import pickle
from game import LineGame
from learning.game_tree import FullGameTree

def game_tree_3x3():
    game = LineGame(3,3)
    start_state = game.get_state_hash()
    tree = FullGameTree()
    tree.dfs(game)
    pickle.dump(tree.state_val, open('data/state_val_3x3.pkl', 'wb'))
    print('\n', len(tree.state_val))
    print(start_state, tree.state_val[start_state])
    for move in game.get_valid_moves():
        game.check_move(move)
        print(game.game_state, tree.state_val[game.get_state_hash()])
        game.delete_move()

if __name__ == '__main__':
    game_tree_3x3()