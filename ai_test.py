from game.ai import AI
from game.piece import PIECE

board = [PIECE.NONE for i in range(9)]

ai = AI(PIECE.O)

board[int(input("move:"))] = PIECE.X

board = ai.move(board)

print (board)

board[int(input("move:"))] = PIECE.X

board = ai.move(board)

print (board)

board[int(input("move:"))] = PIECE.X

board = ai.move(board)

print (board)

board[int(input("move:"))] = PIECE.X

board = ai.move(board)

print (board)
