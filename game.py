
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
        
class Gomoku(Game):
    """Gomoku game rules implementation

    Please note that board x coordinate is horisontal from left to right, 
    board y coordinate is vertical from top to bottom."""

    def __init__(self):
        self.board_size = 15
        self.tokens = ['x', 'o'] # symbols for black and white. Empty cell is None
        self.clean()
        
    def clean(self):
        self.moves = []
        self.board = []
        for x in range(self.board_size):
            self.board.append([])
            for _ in range(self.board_size):
                self.board[x].append(None)
        
    def current_player(self):
        """Number of current player (ie who was the last to move). 0 is black, 1 is white. We assume balck is always first to move."""
        if len(self.moves) % 2 == 0:
            return 1
        return 0

    def add_move(self, move):
        """Record new move."""
        self.moves.append(move)
        self.board[move[0]][move[1]] = self.tokens[self.current_player()]

    def check_move(self, move):
        """Check if the move is valid and records it. Move is a pair of integer coordiantes eg (2, 3)."""
        if move is None:
            return False

        # Out of board
        if move[0] < 0 or move[0] >= self.board_size or move[1] < 0 or move[1] >= self.board_size:
            return False

        # Already on the board
        if self.board[move[0]][move[1]] is not None:
            return False

        self.add_move(move)
        return True

    def check_win(self):
        """Check if this is a winnig game state (eg we have a line of length 5 for current player)."""

        max_len = 5 # length of line to win
        curr_tok = self.tokens[self.current_player()]

        # check columns
        for nrow in range(self.board_size):
            line_len = 0
            for ncol in range(self.board_size):
                if self.board[nrow][ncol] == curr_tok:
                    line_len += 1
                else:
                    line_len = 0
                if(line_len == max_len):
                    return True

        # check rows
        for ncol in range(self.board_size):
            line_len = 0
            for nrow in range(self.board_size):
                if self.board[nrow][ncol] == curr_tok:
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
                    if self.board[nrow][ncol] == curr_tok:
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
                    if self.board[nrow][ncol] == curr_tok:
                        line_len += 1
                    else:
                        line_len = 0
                    if(line_len == max_len):
                        return True


        return False
