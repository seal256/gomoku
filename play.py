#!/usr/bin/env python

import argparse
from importlib import import_module
from gui import BoardGame
from game import LineGame

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gomoku game interface.')
    parser.add_argument('--player', type=str, default='players.perfect3x3', help='Name of file with program for computer player.')
    parser.add_argument('--color', type=str, default='black', help='Color of computer player (black or white).')
    args = parser.parse_args() 

    player = import_module(args.player).player() # call player class constructor
    game = LineGame(3, 3)
    board = BoardGame(game, player, args.color)



