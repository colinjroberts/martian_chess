# Martian Chess in Python
This project is an educational Python implementation of Martian Chess, a game by Looney Labs.
Information about the game and how to play can be found in the main game loop. 

## TODOS
- Implement computer players (at the moment only human v human works)
- Implement game tests
- Refactor Board to accept a board state for initialization (to allow faster testing)
- Add shortcuts for exiting a game
- Add game saving

## Brainstorming 

### Containers
- Board state
  - matrix holding piece objects
  - two lists for holding each players pieces
- Move list using text representation

### Variables
- Player turn marker
- Piece count on each side
- Player Points
- Most recent move (to be used when checking for move backs)

### Methods
- generateBoard() -> bool, returns True when board is set up
- isGameFinished() ->  bool, returns True when game is over or maybe have variable?
- changePlayer() ->  str, returns current player
- updateMostRecentMove() ->  None, sets most recent move
- incrementPoints() ->  int, returns player's score
- movePiece(piece+location, destination) ->  str, returns move for move list
- choosePiece() ->  str, returns chosen piece
- chooseMove() ->  str, returns chosen destination for piece
- collectMoves(location, piece) -> [str], returns list of moves
- playGame(numHumanPlayers) -> None, sets up board, starts game loop

### Classes
- Game (players, score, most recent move, piece count, move list, repl, turn marker)
- Board (width, height, data representing each square, repr)
- Piece (location, movement abilities, point value)
  - Queen χ?
  - Drone δ?
  - Pawn π?

### Play
- Choose a piece
- Choose a valid move 
- Add move to move list
- If piece is captured, increment points
- Update most recent move 
- Check if game is over
- Change player turn
- Repeat

### Choose a piece
- Choose a piece (if datastruct is easy)
- Choose a valid move
  - Start on square and check each path square by square
    - If P, check NE, SE, SW, NW - 1 time
    - If D, check N,E,S,W - 2 times each 
    - If Q, check N, NE, E, SE, S, SW, W, NW - unlimited times
    - Note that max N/S is 8, max E/W is 4, max diags are 4
  - Given location, calculate max path in direction
    - if blocked or out of bounds, return and stop that direction
    - if valid move, add to list of moves and possible try again
  - Choose one valid move from list
  - Check to see if piece is captured
    - if so, remove captured piece and increment points

### Check if game is over
- Check player piece lists, if either is empty, set game over flag

### Change player turn
- If game is not over, increment player

### Questions
- What do moves look like?
  - A queen moves around: 8aQd8, 8aQa1, 8aQd5 
  - A queen moves and captures: 8aQa1-D, 7aQd4-P
  - Two pawns are promoted: 3bPc3+D
  - Pawn and Drone are promoted: 2bPc2+Q
  - I know the promotion is a little redundant, but I think it could be helpful