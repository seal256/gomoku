from game import LineGame
from game_tree import FullGameTree

def game_tree_3x3():
    game = LineGame(3,3)
    tree = FullGameTree(game)

if __name__ == '__main__':
    game_tree_3x3()