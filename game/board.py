import pygame

from .piece import PIECE
from framework.text import Text


def pieceToString(piece, position=" "):
    return "X" if piece is PIECE.X else "O" if piece is PIECE.O else position


class Board:
    def __init__(self, director, rect, player_one, player_two):
        self.director = director
        self.rect = rect
        self.player_one = player_one
        self.player_two = player_two
        self.pieces = [PIECE.NONE for i in range(9)]
        self.winner = PIECE.NONE
        self.is_full = False

        text_height = int(rect.height * .1)
        text_rect = pygame.Rect(rect.x, rect.y, rect.width / 2, text_height)

        self.player_one_text = Text(text_rect, text_height, director.regular_text_color,
                                    director.screen, player_one.name + " [" + pieceToString(player_one.piece) + "]")

        text_rect.top = text_rect.bottom

        self.player_one_score = Text(text_rect, text_height, director.regular_text_color,
                                     director.screen, str(player_one.score))

        text_rect.top = 0
        text_rect.left = text_rect.right

        self.player_two_text = Text(text_rect, text_height, director.regular_text_color,
                                    director.screen, player_two.name + " [" + pieceToString(player_two.piece) + "]")

        text_rect.top = text_rect.bottom

        self.player_two_score = Text(text_rect, text_height, director.regular_text_color,
                                     director.screen, str(player_two.score))

        self.pieces_texts = []

        x = rect.x
        y = self.player_one_score.rect.bottom + 2
        width = int(rect.width / 3)
        height = int((rect.height * .8) / 3)

        square = pygame.Rect(x, y, width, height)

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "1")))

        square.x += width

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "2")))

        square.x += width

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "3")))

        square.x = x
        square.y += height

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "4")))

        square.x += width

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "5")))

        square.x += width

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "6")))

        square.x = x
        square.y += height

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "7")))

        square.x += width

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "8")))

        square.x += width

        self.pieces_texts.append(Text(square, height, director.regular_text_color,
                                      director.screen, pieceToString(PIECE.NONE, "9")))

    def render(self):
        self.player_one_text.render()
        self.player_one_score.render()
        self.player_two_text.render()
        self.player_two_score.render()

        screen = self.director.screen

        x = self.rect.x
        y = self.player_one_score.rect.bottom + 2
        width = int(self.rect.width / 3)
        height = int((self.rect.height * .8) / 3)

        pygame.draw.line(screen, self.director.regular_text_color, (x + width, y),
                         (x + width, self.rect.height - 4))

        pygame.draw.line(screen, self.director.regular_text_color, (x + width * 2, y),
                         (x + width * 2, self.rect.height - 4))

        pygame.draw.line(screen, self.director.regular_text_color, (x + 2, y + height),
                         (x + self.rect.width - 2, y + height))

        pygame.draw.line(screen, self.director.regular_text_color, (x + 2, y + (height * 2)),
                         (x + self.rect.width - 2, y + (height * 2)))

        for indx, piece in enumerate(self.pieces_texts):
            piece.text = pieceToString(self.pieces[indx], str(indx + 1))
            piece.prep_img()
            piece.render()

    def reset(self):
        self.pieces.fill(PIECE.NONE)
        self.winner = PIECE.NONE
        self.is_full = False

    def check(self):
        if self.pieces[0] == self.pieces[1] and self.pieces[1] == self.pieces[2]:
            self.winner = self.pieces[0]
        elif self.pieces[0] == self.pieces[3] and self.pieces[3] == self.pieces[6]:
            self.winner = self.pieces[0]
        elif self.pieces[0] == self.pieces[4] and self.pieces[4] == self.pieces[8]:
            self.winner = self.pieces[0]
        elif self.pieces[1] == self.pieces[4] and self.pieces[4] == self.pieces[7]:
            self.winner = self.pieces[1]
        elif self.pieces[2] == self.pieces[4] and self.pieces[4] == self.pieces[6]:
            self.winner = self.pieces[2]
        elif self.pieces[2] == self.pieces[5] and self.pieces[5] == self.pieces[8]:
            self.winner = self.pieces[2]
        elif self.pieces[3] == self.pieces[4] and self.pieces[4] == self.pieces[5]:
            self.winner = self.pieces[3]
        elif self.pieces[6] == self.pieces[7] and self.pieces[7] == self.pieces[8]:
            self.winner = self.pieces[6]
