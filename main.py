import Game

def print_welcome():
  print(
  """
  =================================================
   __  __    __    ____  ____  ____    __    _  _   
  (  \/  )  /__\  (  _ \(_  _)(_  _)  /__\  ( \( )
   )    (  /(  )\  )   /  )(   _)(_  /(  )\  )  ( 
  (_/\/\_)(__)(__)(_)\_) (__) (____)(__)(__)(_)\_) 
    ___  _   _  ____  ___  ___
   / __)( )_( )( ___)/ __)/ __)
  ( (__  ) _ (  )__) \__ \\\\__ \\
   \___)(_) (_)(____)(___/(___/
  -------------------------------------------------
  An unlicesned digital reporduction of the game 
  invented by Andrew Looney / Looney Labs.
  =================================================\
  """
  )
  return

def print_rules():
  print(
  """
  Martian chess is a turn-based strategy game played on a 
  grid by (in this implementation) two players. Each player 
  controls the pieces on their half of the grid. The players 
  take turns, moving one piece at a time, potentially 
  capturing opponent pieces to score points. The game ends 
  when either side of the board has no pieces on it. When the 
  game ends, the winner is the player with the most points. 

  -----------------------------------------------------
  Pieces

  There are three types of pieces:
  - Pawns, worth one point when captured, can move one 
    space diagonally. 
  - Drones, worth two points when captured, can move one or 
    two spaces vertically and horizontally.
  - Queens, worth three points when captured, can move any 
    number of spaces in any direction.

  -----------------------------------------------------
  Board Setup

  The board (at least in this version) is a 4x8 grid. Pieces 
  begin in the following rotationally symmetric layout:

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

  -----------------------------------------------------
  Taking Turns

  In this implementation, Player 1 always goes first. Players 
  take turns moving one piece per turn. A player controls any 
  and all pieces on their half of the board. For example, if
  Player 2 moves a Drone from 6a to 4a, Player 1 controls the 
  drone on their next turn because it is on their half of the
  board. 

  An important note, is that on the player's turn immediately 
  following a piece changing sides (Player 1's turn in the 
  previous example), that player is not allowed to move the 
  newly controllable piece to the position it just came from. 
  In that example, Player 2 moved the Drone from 6a to 4a. 
  Player 1, on this next turn only, is prohibitted from 
  returning that same Drone to 6a. Moving the Drone to 5a 
  is a valid move.

  Pieces cannot move through or jump over other pieces; 
  that is, they must have an open path to their destination.
  For example, on Player 1's opening move, no Wueen can 
  move because all paths are blocked nor can the Drone at 
  2c move because all of its baths are also blocked. 

  Pieces can be moved either to an unoccupied square, or a
  square on the opponent's side of the board that has a piece
  on it. Moving to the same square as an opponent's piece
  captures that piece. The piece is removed from the board,
  and the player making the capturing move receives points.

  Pieces can only be captured from the opponents side of the
  board; remember that any piece on your side of the board
  is your piece.

  There are two situations in which you can move a piece onto
  one of your own occupied squares:
  - If you have no Queens, a Drone can be moved onto a Pawn's
  square (or vice versa) to be promoted to a new Queen. The 
  Pawn and Drone are removed from the game, no points are awarded.
  - If you have no Drones, a Pawn can be moved onto another
  Pawn's square to be promoted to a new Drone. The two Pawns 
  are removed from the game, no points are awarded.

  -----------------------------------------------------
  Ending the Game

  The game ends when either half of the board is empty for 
  any reason. There may or may not be many pieces left on 
  the board. After a piece crosses the threshold leaving
  the board empty, process a capture if it occured, then the
  game is over. 

  The player with the most points wins.\
  """
  )
  return

def print_how_to_play():
  print(
  """
  On your turn, the game will prompt you to enter a move. 
  In this implementation, moves are entered using the 
  following notation that describes the starting location
  of a piece, the type of piece, and the ending location 
  of a piece. For example, moving a Pawn from 3c to 4d 
  would be represented as `3cPd4`. 

  The order in which the letter and number of the square
  does not matter. `3cPd4`, `3cP4d`, `c3Pd4`, and `c3Pd4`
  all describe the same move. We prefer the first notation
  partially because it is weird and that is interesting and
  fun, and partially because it makes checking for whether 
  or not a piece is moving back to the square it came from 
  easier to notice visually. A move returning to the starting 
  location of the previous move is a reflection of the previous
  move. For example, after the move `3dDd5`, `5dDd3` would 
  not be a valid move. Ok...the notation is mostly because it 
  is novel and fun.

  Though you need only type in your move, this notation can 
  describe game events like piece captures and promotions. 
  Captures are noted with a minus sign and the piece that was
  captured. Promotions are noted with a plus sign and the piece
  that is added.

  Consider the following opening moves in which Player 1 moves
  a Pawn from 3b to 4a and Player 2 captures the Pawn with a 
  Drone by moving it two spaces from 6a to 4a:


        a b c d       a b c d       a b c d
      8  Q|Q|D|_    8  Q|Q|D|_    8  Q|Q|D|_
  P   7  Q|D|P|_    7  Q|D|P|_    7  Q|D|P|_
  2   6  D|P|P|_    6  D|P|P|_    6  _|P|P|_ 
      5  _|_|_|_    5  _|_|_|_    5  _|_|_|_  
      4  _|_|_|_    4  P|_|_|_    4  D|_|_|_
  P   3  _|P|P|D    3  _|_|P|D    3  _|P|P|D
  1   2  _|P|D|Q    2  _|P|D|Q    2  _|P|D|Q
      1  _|D|Q|Q    1  _|D|Q|Q    1  _|D|Q|Q
        a b c d       a b c d        a b c d 

        Setup         Turn 1         Turn 2

  These moves would be represented as follows:
  3bPa4,6aDa4-P

  Move history will be displayed along side the current
  state of the board. Consider the following game in 
  progress in which it is Player 2's turn on round 7:


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
  )
  return

def print_credits():
  print(
  """
  Martian Chess was invented by Andrew Looney in 1999. The 
  official game is released by Looney Labs and historically
  retails for about $20 USD. 

  This implementation was made as a personal project without 
  the consent or endorsement of Looney Labs by Colin Roberts.\
  """
  )
  return

def play_game():
  print(
  """
  This game will have 2 players, P1 and P2. 
  Choose one of the following options:
  1 - Human player 1, computer player 2
  2 - Computer player 1, human player 2
  3 - Human players 1 and 2
  4 - Computer players 1 and 2
  """
  )

  player_options = {
    "1": ["h", "c"],
    "2": ["c", "h"],
    "3": ["h", "h"],
    "4": ["c", "c"],
  }

  choice = input("\n>")
  # Game takes a list of human players
  game = Game.Game(player_options[choice])

  print("Look you are playing the game!")
  return

def print_choices():
  print(
  """
  Please enter one of the following options:
    1 - Play Martian Chess
    2 - Rules of the game
    3 - Notes on how to play
    4 - Credits 
    5 - Exit\
  """
  )
  return

def run():
  menu_options = {
    "0": print_welcome,
    "1": play_game,
    "2": print_rules,
    "3": print_how_to_play,
    "4": print_credits,
    "5": quit
  }
  choice = "0"
  while choice in menu_options:
    menu_options[choice]()
    print_choices()
    choice = input("\n> ")

if __name__ == "__main__":
  run()

