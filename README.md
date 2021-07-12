# Martian Chess in Python

-----------------------------------------------------
## Ideas

State of the board
list of moves 
  could be start and finish coordinate, piece name for reading
notation for capture
  Q1d 7dxQ 
keep track of points

P1, P2
P1 is on the bottom, always goes first


-----------------------------------------------------
# Containers
- Board state
  - matrix holding piece objects
  - two lists for holding each players pieces
- Move list using text representation

-----------------------------------------------------
# Variables
- Player turn marker
- Piece count on each side
- Player Points
- Most recent move (to be used when checking for move backs)

-----------------------------------------------------
## Methods
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


-----------------------------------------------------
## Classes
- Game (players, score, most recent move, piece count, move list, repl, turn marker)
- Board (width, height, data representing each square, repr)
- Piece (location, movement abilities, point value)
  - Queen χ?
  - Drone δ?
  - Pawn π?


-----------------------------------------------------
## Play
- Choose a piece
- Choose a valid move 
- Add move to move list
- If piece is captured, increment points
- Update most recent move 
- Check if game is over
- Change player turn
- Repeat

-----------------------------------------------------
## Choose a piece
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

##  Check if game is over
- Check player piece lists, if either is empty, set game over flag

## Change player turn
- If game is not over, increment player

# Repeat


## Program REPL
- run
- welcome
  - 1) play
  - 2) instructions
  - 3) credits


play
- how many players (1-4)?
- Of those, which are human (just collect numbers and split)?
- Create board
- Start game loop

-----------------------------------------------------
# Questions
- What do moves look like?
  - A queen moves around: 8aQd8, 8aQa1, 8aQd5 
  - A queen moves and captures: 8aQa1-D, 7aQd4-P
  - Two pawns are promoted: 3bPc3+D
  - Pawn and Drone are promoted: 2bPc2+Q
  - I know the promotion is a little redundant, but I think it could be helpful


Board is small and whole thing could be a matrix
```
[
[[Q], [Q], [D], [ ]]
[[Q], [D], [P], [ ]]
[[D], [P], [P], [ ]]
[[ ], [ ], [ ], [ ]]
[[ ], [ ], [ ], [ ]]
[[ ], [P], [P], [D]]
[[ ], [P], [D], [Q]]
[[ ], [D], [Q], [Q]]
]
```

```
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

For ease, split board state into halves
Q8a,Q8b,D8c,Q7a,D7b,P7c,D6a,P6b,P6c
P3b,P3c,D3c,P2b,D2c,Q2d,D1c,Q1c,Q1d

8aQ,8bQ,8cD,7aQ,7bD,7cP,6aD,6bP,6cP
3bP,3cP,3cD,2bP,2cD,2dQ,1cD,1cQ,1dQ

```