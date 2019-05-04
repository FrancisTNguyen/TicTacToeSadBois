from .piece import PIECE
import time
import random


class AI:

    #initiate the pieces
    def __init__(self, piece):
        self.piece = piece
        self.myBoard = []

        if piece == PIECE.X:
            self.opponents_piece = PIECE.O
        else:
            self.opponents_piece = PIECE.X

    #populate a list with optimal moves that the AI can take
    # def move(self, board):
    #     best = self.minimax(board, True)

    #     #since there's two elements in best.  if the right element is not -1 then that is the board's best move
    #     if best[1] != -1:
    #         board[best[1]] = self.piece

    #     time.sleep(1)
    #     print(best)
    #     return board

    #Problem: this AI only makes the best move that would result it in winning the game
    #it does not actually block the player's move if they are about to win.


    #This is a sample pseudo code.  May need to put this into minimax because it's gonna be the best move that the AI should make.
    #Move every element in best down 1, and then append the blocking move onto the first of the best list
    #def winCondition(self, board)
    #   if(pieces > 1)
    #          grab the cell number that has the winning condition
    #          piece.x/o  = winning cell
    #          move best elements down 1
    #          blocking move = best[0]
    #          return best    

    def isSpaceFree(self, board, move):
        # Return True if the passed move is free on the passed board.
        return board[move] == 0

    def chooseRandomMoveFromList(self, board, moveList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []

        for i in moveList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None



    def moveTest(self, board, piece, indexMove):
        board[indexMove] = piece
    #we need to return the whole board with the moves given
    def move(self, board):
        # we need to find out a way to make a move here from a function that tells us
        # where to move
        # best = function call to the function you are about to create from Ian's code
        best = self.minimax(board, True)
        board[best] = self.piece
        return board

    def copyBoard(self, board):
        self.myBoard = board #this should create a local copy of the board

    def minimax(self, board, maximize):
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
        movesAvailable = self.getEmptyIndexies(board)
        for i in movesAvailable:
            boardCopy = board
            self.moveTest(boardCopy, self.piece, i)
            if self.getWinner(boardCopy):
                    return i

    # Check if the player could win on their next move and block them.
        for i in movesAvailable:
            boardCopy = board
            self.moveTest(boardCopy, self.opponents_piece, i)
            if self.getWinner(boardCopy):
                    return i

    # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def getEmptyIndexies(self, board):
        return [item for item, piece in enumerate(board) if piece == PIECE.NONE]

    def getBoardScoreForPiece(self, board):
        winner = self.getWinner(board)

        if self.piece == winner:
            return 7
        elif self.opponents_piece == winner:
            return -7
        return 0

    def getWinner(self, board):
        if board[0] == board[1] and board[1] == board[2] and board[0] != PIECE.NONE:
            return board[0]
        elif board[0] == board[3] and board[3] == board[6] and board[0] != PIECE.NONE:
            return board[0]
        elif board[0] == board[4] and board[4] == board[8] and board[0] != PIECE.NONE:
            return board[0]
        elif board[1] == board[4] and board[4] == board[7] and board[0] != PIECE.NONE:
            return board[1]
        elif board[2] == board[4] and board[4] == board[6] and board[0] != PIECE.NONE:
            return board[2]
        elif board[2] == board[5] and board[5] == board[8] and board[0] != PIECE.NONE:
            return board[2]
        elif board[3] == board[4] and board[4] == board[5] and board[0] != PIECE.NONE:
            return board[3]
        elif board[6] == board[7] and board[7] == board[8] and board[0] != PIECE.NONE:
            return board[6]

        return PIECE.NONE
