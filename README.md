# gomoku

Gui for human-AI play. 
Please add your players to folder ./players as separate files. 
A player class instance should implement method get_move(game). 
See crazy.py for example.

To start game with your AI player run
```
pyhton play.py --player players.player_file_name --color color_for_ai
```

Note that black is always first to move.
