import Board
import re


class Game:
    def __init__(self, players):
        self.board = Board.Board(players)
        self.piece_types = ["P", "D", "Q"]
        self.number_of_players = len(players)
        self.players = players
        self.turn = 1
        self.move_list = []
        self.most_recent_move = ""
        self.scores = {
            "1": 0,
            "2": 0,
        }
        self.isFinished = False

        # Main game loop
        while not self.isFinished:

            if self.players[self.turn-1] == "h":
                # human turn
                print(f"Player {self.turn}'s turn. Type in your move.")
                self.human_turn()

            else:
                # computer turn
                print(f"Player {self.turn}'s turn (computer).")
                self.computer_turn()

        self.end_game()

    def human_turn(self):
        print(self)
        move = input("\n")
        move_valid, error_list = self.parse_move(move)
        while not move_valid:
            for e in error_list:
                print(e)
            print("That is not a valid move. Please try entering another move:")
            print(self)
            move = input("\n")
            move_valid, error_list = self.parse_move(move)
        self.scores[str(self.turn)] += self.board.move_piece(move, self.turn)
        self.move_list.append(move)
        self.isFinished = not self.board.count_all_pieces_on_half(1) == 0 and not self.board.count_all_pieces_on_half(2) == 0
        if not self.isFinished:
            self.turn = self.turn % self.number_of_players + 1

    def computer_turn(self):
        pass

    def parse_move(self, move):
        valid = True
        output = False
        move = move.upper()
        error_list = []

        parsing_rules = [
            self.check_move_string_length,
            self.check_move_format_starting_position,
            self.check_move_format_piece,
            self.check_move_format_destination_position,
            self.check_move_start_is_not_end,
            self.check_move_starting_position_on_board,
            self.check_move_starting_position_board_half,
            self.check_move_starting_position_has_piece,
            self.check_move_destination,
            self.check_move_path,
        ]

        for rule in parsing_rules:
            if valid:
                output, error = rule(move)
                error_list.append(error)
                valid = valid and output
        return output, error_list

    def check_move_string_length(self, move):
        if len(move) == 5:
            return True, ""
        else:
            return False, "The move you entered is too long."

    # check that move is made of number+letter or vice versa,
    # then piece type,
    # then another number+letter or vice versa
    def check_move_format_starting_position(self, move):
        start_square = move[:2]
        if re.search("([1-9][a-zA-Z])", start_square) or re.search("([a-zA-Z][1-9])", start_square):
            return True, ""
        else:
            return False, f"The format of the starting position you entered ({start_square}) is incorrect. " \
                          f"It should be one letter and one number."

    def check_move_format_piece(self, move):
        if move[2] in self.piece_types:
            return True, ""
        else:
            return False, f"The format of the piece you typed ({move[2]}) is incorrect. It should be P, D, or Q."

    def check_move_format_destination_position(self, move):
        end_square = move[3:]
        if re.search("([1-9][a-zA-Z])", end_square) or re.search("([a-zA-Z][1-9])", end_square):
            return True, ""
        else:
            return False, f"The format of the destination position you entered ({end_square}) is incorrect. " \
                          f"It should be one letter and one number."

    # checks that the starting position and ending position are not the same
    def check_move_start_is_not_end(self, move):
        if move[:2] != move[3:]:
            return True, ""
        else:
            return False, "The starting square and destination square of your move are the same. " \
                          "A piece must move to a square different from where it started."

            # checks that the starting position is a valid square
    def check_move_starting_position_on_board(self, move):
        start_pos = move[:2]
        if (re.search("([1-8][a-dA-D])", start_pos) or re.search("([a-dA-D][1-8])", start_pos)):
            return True, ""
        else:
            return False, "The starting position of the move you entered is not on the board."

    # check that the piece is on the player's half of the board
    def check_move_starting_position_board_half(self, move):
        start_pos = move[:2]
        if self.turn == self.board.get_board_half(start_pos):
            return True, ""
        else:
            return False, "The starting position of the move you entered is not on your half of the board."

    # check that the piece in the move is currently on that square
    def check_move_starting_position_has_piece(self, move):
        piece_on_board = str(self.board.get_piece(move[:2]))
        if (move[2] == piece_on_board):
            return True, ""
        else:
            return False, f"The piece you chose in your move ({move[2]}) is not on the piece at " \
                          f"square {move[:2]} ({piece_on_board})."

    # checks that the ending position is a valid square
    # and that the position is either on player's half of the board or
    #    on the other half of the board or is a valid promotion
    def check_move_destination(self, move):
        start_pos = move[:2]
        end_pos = move[3:]
        entered_square_validity = (re.search("([1-8][A-D])", end_pos) or re.search("([A-D][1-8])", end_pos))
        location_validity = False
        destination_half_of_board = self.board.get_board_half(end_pos)
        piece_on_destination_square = str(self.board.get_piece(end_pos))
        piece_being_moved = str(self.board.get_piece(start_pos))

        # If on player's half of the board
        if destination_half_of_board == self.turn:
            # If the destination is empty, it's fine
            if piece_on_destination_square == "_":
                location_validity = True
            # If the destination has a piece on it, check for promotion
            else:
                # If no Queens, a Drone and Pawn can be combined
                if self.board.count_this_type_of_piece_on_half(destination_half_of_board, "Queen") == 0 and \
                        (piece_being_moved.piece_type == "Pawn" and piece_on_destination_square.piece_type == "Drone" or \
                         piece_being_moved.piece_type == "Drone" and piece_on_destination_square.piece_type == "Pawn" ):
                    location_validity = True

                # If no Drones, two Pawns can be combined
                elif self.board.count_this_type_of_piece_on_half(destination_half_of_board, "Drone") == 0 and \
                        piece_being_moved.piece_type == "Pawn" and piece_on_destination_square.piece_type == "Pawn":
                    location_validity = True

        # If it is on other side of the board
        elif self.board.get_board_half(move[3:]) != self.turn:
            location_validity = True

        if entered_square_validity and location_validity:
            return True, ""
        else:
            return False, "The destination of your move is not valid either because it isn't a valid square, " \
                          "or it is on your half of the board and isn't a promotion"

    # checks that move is valid for piece
    # and does not go through other pieces
    def check_move_path(self, move):
        start_pos = move[:2]
        path_tuple = self.board.get_path(move)  # tuple of direction and list of squares in path
        piece = self.board.get_piece(start_pos)  # dict with valid "max_distance" and "direction" piece mvmt

        # Check that the piece is allowed to move that number of squares
        if len(path_tuple[0])-1 > piece.max_distance:
            return False, "The move you entered is too far for that piece."

            # Check that piece is allowed to move in that direction
        if path_tuple[0] not in piece.direction:
            return False, "The move you entered is not a valid direction for that piece."

        # Check that path does not contain any other pieces
        path_obstructed = False
        for square in path_tuple[1][1:-1]:
            if str(self.board.get_piece(square)) != "_":
                path_obstructed = True

        if not path_obstructed:
            return True, ""
        else:
            return False, "The path of the movement you entered has a piece in it."

    # returns which player is in the lead
    def get_leader(self):
        highest_score = max(self.scores["1"], self.scores["2"])
        if self.scores["1"] == self.scores["2"]:
            return "1 and 2"
        elif self.scores["1"] == highest_score:
            return "1"
        else:
            return "2"

    def end_game(self):
        print("Player " + self.get_leader() + " is the winner.")
        print("Final state of the board:")
        print(self)
        print("Press any key to return to the main menu")
        input("")

    def __repr__(self):
        output = ""
        brd = str(self.board)
        splt_brd = brd.split("\n")

        # for each line in
        for i, line in enumerate(splt_brd):

            # First line prints scores
            if i == 0:
                output += line + f"       P1:   {self.scores['1']}  P2:   {self.scores['2']}\n"

            # second line on prints board and move list
            elif (len(self.move_list) + 1) // 2 >= i:
                # only 1 or 2 moves left to print
                if (len(self.move_list) + 1) // 2 == i:
                    output += line + f"    {i}  {self.move_list[i-1]}"
                    if len(self.move_list) % 2 == 0:
                        output += f"    {self.move_list[i]}"
                    output += "\n"

                # printing whole lines
                else:
                    output += line + f"    {i}  {self.move_list[i-1]}    {self.move_list[i]}\n"
            else:
                output += line + "\n"
        return output

        # split up the board repr by line and add the score and moves to the list
        """
             a b c d       P1:   4  P2:   2
          8  Q|_|_|D    1  3cPb4    6cPd5
      P   7  Q|D|_|_    2  2cDc3    7cPd6
      2   6  D|_|_|P    3  3dDd5-P  8bQc7
          5  _|_|P|P    4  3bPc4    8cDd8
          4  _|_|_|Q    5  4cPd6-D  7cQc3-D
      P   3  _|_|_|_    6  3cQd4    6bPc5
      1   2  _|P|_|Q    7  4bPc5-P
          1  _|D|Q|Q
             a b c d\
        """

