from copy import deepcopy

class Game(object):
    """Abstract inrterface for game rules.
    Please implement all methods in a child class.
    """

    def __init__(self):
        raise NotImplementedError
    
    def check_move(self, move):
        """Check if the move is valid and records it."""
        raise NotImplementedError

    def check_win(self):
        """Check if this is a winnig game state."""
        raise NotImplementedError

class GameState:
    """Keeps only game state, ignoring move history."""

    def __init__(self, board_size, default_token):
        self.board_size = board_size
        self.clean(default_token)

    def clean(self, default_token):
        self.board = [default_token] * (self.board_size * self.board_size)

    def update(self, move, token):
        self.board[move[1] * self.board_size + move[0]] = token

    def get_token(self, move):
        return self.board[move[1] * self.board_size + move[0]]

    def __str__(self):
        s = ''
        for x in range(self.board_size):
            for y in range(self.board_size):
                s += str(self.get_token((x,y)))
            s += '\n'
        return s

class LineGame(Game):
    """Gomoku game rules implementation

    Please note that board x coordinate is horisontal from left to right, 
    board y coordinate is vertical from top to bottom."""

    def __init__(self, board_size, win_line_len):
        self.tokens = ['x', 'o'] # symbols for black and white. Empty cell is None
        self.no_token = '.' # empty cell token
        self.board_size = board_size
        self.game_state = GameState(self.board_size, self.no_token)

        self.win_line_len = win_line_len
        self.clean()
        self.max_moves = self.board_size * self.board_size
        
    def clean(self):
        self.game_state.clean(self.no_token)
        self.moves = []
        self.valid_moves = set()
        
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.valid_moves.add((x,y))
        
    def current_player(self):
        """Number of current player (ie who was the last to move). 0 is black, 1 is white. We assume balck is always first to move."""
        if len(self.moves) % 2 == 0:
            return 1
        return 0

    def current_player_token(self):
        return self.tokens[self.current_player()]

    def add_move(self, move):
        """Record new move."""
        self.moves.append(move)
        self.valid_moves.discard(move)
        self.game_state.update(move, self.current_player_token())

    def delete_move(self):
        """Delete last move."""
        move = self.moves.pop()
        self.valid_moves.add(move)
        self.game_state.update(move, self.no_token)

    def get_valid_moves(self):
        return deepcopy(self.valid_moves)

    def get_state_hash(self):
        return ''.join(self.game_state.board)

    #def get_successor_state(self, board, move, current_player):
    #    board = deepcopy(self.game_state)
    #    board[move[0]][move[1]] = self.tokens[current_player]
    #    return board

    def check_move(self, move):
        """Check if the move is valid and records it. Move is a pair of integer coordiantes eg (2, 3)."""
        if move is None:
            return False

        # Out of board
        if move[0] < 0 or move[0] >= self.board_size or move[1] < 0 or move[1] >= self.board_size:
            return False

        # Already on the board
        if self.game_state.get_token(move) is not self.no_token:
            return False

        self.add_move(move)
        return True

    def check_win(self):
        """Check if this is a winnig game state (eg we have a line of winning length for current player)."""

        max_len = self.win_line_len # length of line to win
        curr_tok = self.tokens[self.current_player()]

        # check columns
        for nrow in range(self.board_size):
            line_len = 0
            for ncol in range(self.board_size):
                if self.game_state.get_token((nrow, ncol)) == curr_tok:
                    line_len += 1
                else:
                    line_len = 0
                if(line_len == max_len):
                    return True

        # check rows
        for ncol in range(self.board_size):
            line_len = 0
            for nrow in range(self.board_size):
                if self.game_state.get_token((nrow, ncol)) == curr_tok:
                    line_len += 1
                else:
                    line_len = 0
                if(line_len == max_len):
                    return True

        # check diagonals top left to bottom right
        start_pos = [(0, n) for n in range(self.board_size - max_len + 1)] + \
            [(n, 0) for n in range(1, self.board_size - max_len + 1)] # start positions for diagonals

        for x_start, y_start in start_pos:
            line_len = 0
            diag_len = self.board_size - max(x_start, y_start)
            for n in range(0, diag_len):
                    nrow = x_start + n
                    ncol = y_start + n
                    if self.game_state.get_token((nrow, ncol)) == curr_tok:
                        line_len += 1
                    else:
                        line_len = 0
                    if(line_len == max_len):
                        return True

        # check diagonals top right to bottom left
        start_pos = [(n, 0) for n in range(max_len - 1, self.board_size)] + \
            [(self.board_size - 1, n) for n in range(1, self.board_size - max_len + 1)] # start positions for diagonals

        for x_start, y_start in start_pos:
            line_len = 0
            diag_len = min(x_start + 1, self.board_size - y_start)
            for n in range(0, diag_len):
                    nrow = x_start - n
                    ncol = y_start + n
                    if self.game_state.get_token((nrow, ncol)) == curr_tok:
                        line_len += 1
                    else:
                        line_len = 0
                    if(line_len == max_len):
                        return True

        if len(self.moves) == self.max_moves: # draw
            return None
        
        return False
