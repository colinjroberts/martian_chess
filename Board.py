import Piece
import re

# noinspection SpellCheckingInspection
class Board:
    # Starting locations should match
    """
       Player 2
       a b c d
    8  Q|Q|D|_
    7  Q|D|P|_
    6  D|P|P|_
    5  _|_|_|_
    4  _|_|_|_
    3  _|P|P|D
    2  _|P|D|Q
    1  _|D|Q|Q
       a b c d
       Player 1
  """

    starting_locations = {
        "Queen": ["1D", "1C", "2D", "8A", "8B", "7A", ],
        "Drone": ["1B", "2C", "3D", "6A", "7B", "8C", ],
        "Pawn": ["2B", "3B", "3C", "6B", "6C", "7C", ],
    }

    num_value_for_letter = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
    }

    def __init__(self, players):
        self.P1 = players[0]
        self.P2 = players[1]
        self.width = 4
        self.height = 8
        self.board = self.create_empty_board()
        self.populate_board()

    # Board conversion chart
    """
       Player 2
        a  b  c  d
    8  28|29|30|31
    7  24|25|26|27
    6  20|21|22|23
    5  16|17|18|19
    4  12|13|14|15
    3   8| 9|10|11
    2   4| 5| 6| 7
    1   0| 1| 2| 3
        a  b  c  d 
       Player 1
    """

    def convert_position_to_list_index(self, position):
        letter_part = 0
        number_part = 0
        # split up position into number and letter parts
        splits = re.split(r"([a-zA-Z])", position)
        for subposition in splits:
            if re.search("[a-zA-Z]", subposition):
                letter_part = int(self.num_value_for_letter[subposition])
            elif re.search("[1-8]", subposition):
                number_part = int(subposition)
        # convert to index
        output = int(self.width * number_part - 1 - (self.width - letter_part))
        return output
        # 5 * 5 - 1 - (4 - 2) = 25 - 1 - 2 = 22
    def convert_list_index_to_position(self):
        pass

    def create_empty_board(self):
        return [Piece.Piece() for x in range(self.width * self.height)]

    # Places pieces on the board using starting_locations
    def populate_board(self):
        for piece in self.starting_locations:
            for location in self.starting_locations[piece]:
                self.board[self.convert_position_to_list_index(location)] = Piece.Piece(piece)

    # assumes move is valid
    # moves a piece and handles capturing and promoting
    # returns points that are to be added to current player's score
    def move_piece(self, move, player):
        # if destination is empty
        piece_on_destination = self.get_piece(move[3:])

        # move piece return zero
        if str(piece_on_destination) == "_":
            piece_to_move = self.get_piece(move[:2])  # save piece
            self.set_piece(move[:2], Piece.Piece())   # clear starting square
            self.set_piece(move[3:], piece_to_move)   # place piece in destination
            return 0

        # if destination has a piece in it
        else:
            # if it is on player's half - promote
            if self.get_board_half(move[3:]) == player:
                # promote the piece
                return 0
            # otherwise it must be a capture
            else:
                piece_to_move = self.get_piece(move[:2])  # save piece
                print(f"Valid move! Moving {piece_to_move} from {move[:2]} to {move[3:]}")
                self.set_piece(move[:2], Piece.Piece())   # clear starting square
                self.set_piece(move[3:], piece_to_move)   # put piece in destination
                return piece_on_destination.value

        return 0

    def get_piece(self, square):
        return self.board[self.convert_position_to_list_index(square)]

    def set_piece(self, square, piece):
        index = self.convert_position_to_list_index(square)
        self.board[index] = piece
        return

    # returns which half of the board the piece is on (1 or 2)
    def get_board_half(self, square):
        if self.convert_position_to_list_index(square) <= ((self.width * self.height) / 2) - 1:
            return 1
        else:
            return 2

    # Returns a list of all squares in a move including starting and ending square
    def get_path(self, move):
        output_list = []
        move_type = ""
        letters = re.findall("[a-zA-Z]", move)
        numbers = re.findall("[1-8]", move)

        # Add starting square
        output_list.append(letters[0] + numbers[0])

        if letters[0] != letters[2] and numbers[0] != numbers[1]:
            move_type = "d"
            #   both letter and number are different (diagonal movement)
            #       they should always increment at the same rate
            distance = abs(ord(letters[2]) - ord(letters[0]))

            letter_direction = (ord(letters[2]) - ord(letters[0])) // abs(ord(letters[2]) - ord(letters[0]))
            number_direction = (int(numbers[1]) - int(numbers[0])) // abs(int(numbers[1]) - int(numbers[0]))

            # considers all letters not including start nor end
            range_letters = [chr(i) for i in range(ord(letters[0]) + letter_direction, ord(letters[2]), letter_direction)]
            range_numbers = [str(i) for i in range(int(numbers[0]) + number_direction, int(numbers[1]), number_direction)]

            # print(range_numbers, letter_direction, range_letters, number_direction)

            for i in range(len(range_letters)):
                output_list.append(range_letters[i] + range_numbers[i])

        elif letters[0] != letters[2]:
            move_type = "h"
            distance = abs(ord(letters[2]) - ord(letters[0]))
            direction = (ord(letters[2]) - ord(letters[0])) // distance
            # considers all letters not including start nor end
            for i in range(ord(letters[0]) + direction, ord(letters[2]), direction):
                output_list.append(chr(i) + numbers[1])

        else:
            move_type = "v"
            direction = (int(numbers[1]) - int(numbers[0])) // abs(int(numbers[1]) - int(numbers[0]))
            # considers all numbers not including start nor end
            # [print(numbers, direction)]
            for i in range(int(numbers[0]) + direction, int(numbers[1]), direction):
                output_list.append(letters[0] + str(i))

        # Add end square
        output_list.append(letters[2] + numbers[1])
        return (move_type, output_list)

    def count_all_pieces_on_half(self, board_half):
        board_search_range = []
        if board_half == 1:
            board_search_range.append(0)
            board_search_range.append(self.height * self.width * 2)
        else:
            board_search_range.append(self.height * self.width * 2 - 1)
            board_search_range.append(self.height * self.width)
        return sum(1 for p in self.board[board_search_range[0]:board_search_range[1]] if str(p) != "_")

    def count_this_type_of_piece_on_half(self, board_half, piece_type):
        board_search_range = []
        if board_half == 1:
            board_search_range.append(0)
            board_search_range.append(self.height * self.width * 2)
        else:
            board_search_range.append(self.height * self.width * 2 - 1)
            board_search_range.append(self.height * self.width)
        return sum(1 for p in self.board[board_search_range[0]:board_search_range[1]] if p.piece_type == piece_type)


    # pretty print!
    def __repr__(self):
        """
          a b c d
       8  Q|Q|D|_
    P  7  Q|D|P|_
    2  6  D|P|P|_
       5  _|_|_|_
       4  _|_|_|_
    P  3  _|P|P|D
    1  2  _|P|D|Q
       1  _|D|Q|Q
          a b c d
    """

        s = """\
      a b c d
"""
        for i in range(8, 0, -1):
            if i == 8:
                s += "P  "
            elif i == 7:
                s += "2  "
            elif i == 3:
                s += "P  "
            elif i == 2:
                s += "1  "
            else:
                s += "   "
            s += f"""{i}  \
{self.board[i * self.width - 4]}|\
{self.board[i * self.width - 3]}|\
{self.board[i * self.width - 2]}|\
{self.board[i * self.width - 1]}
"""

        s += """\
      a b c d\
"""

        return s
