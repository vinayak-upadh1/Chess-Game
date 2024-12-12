import os
import pygame

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Piece:
    def __init__(self, size):
        self.size = size
        self.piece = {
            "black bishop": BASE_PATH + "/assets/B_BISHOP.png",
            "black king": BASE_PATH + "/assets/B_KING.png",
            "black knight": BASE_PATH + "/assets/B_KNIGHT.png",
            "black pawn": BASE_PATH + "/assets/B_PAWN.png",
            "black queen": BASE_PATH + "/assets/B_QUEEN.png",
            "black rook": BASE_PATH + "/assets/B_ROOK.png",
            "white bishop": BASE_PATH + "/assets/W_BISHOP.png",
            "white king": BASE_PATH + "/assets/W_KING.png",
            "white knight": BASE_PATH + "/assets/W_KNIGHT.png",
            "white pawn": BASE_PATH + "/assets/W_PAWN.png",
            "white queen": BASE_PATH + "/assets/W_QUEEN.png",
            "white rook": BASE_PATH + "/assets/W_ROOK.png",
        }

    def get_piece(self, piece_name):
        piece = self.piece.get(piece_name, None)
        if piece is None:
            return None
        return pygame.transform.smoothscale(pygame.image.load(piece), self.size)
