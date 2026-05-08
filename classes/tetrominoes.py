"""Tetrominoes are the shapes of squares that are controlled by the player"""
import os

import numpy as np
import pygame
import sys

from classes.blocks import Block

dark_blue = pygame.image.load(os.path.join('images', 'dark_blue.png'))
light_blue = pygame.image.load(os.path.join('images', 'light_blue.png'))
yellow = pygame.image.load(os.path.join('images', 'yellow.png'))
red = pygame.image.load(os.path.join('images', 'red.png'))
purple = pygame.image.load(os.path.join('images', 'purple.png'))
orange = pygame.image.load(os.path.join('images', 'orange.png'))
green = pygame.image.load(os.path.join('images', 'green.png'))


class Tetromino:
    """This is the superclass for every possible tetromino"""

    def __init__(self, color, size, x_offset):
        self.color = pygame.transform.scale(color, (size, size))
        self.rotating_state = 0
        self.x_offset = x_offset

    def drop(self):
        """Every second, the tetromino drops one tile further to the ground"""
        for block in self.squares:
            block.y += 1

    def draw(self, window, size, state=0):
        # state 0: on board
        # state 1: holding
        # state 2: next
        for block in self.squares:
            block.draw(window, size, state, self.x_offset)

    def rotate(self, a):
        pass

    def check_lost(self, setup):
        for block in self.squares:
            if setup[block.y][block.x]:
                self.lose()

    @staticmethod
    def lose():
        pygame.quit()
        sys.exit()


class Straight(Tetromino):
    """The long straight light blue tetromino"""

    def __init__(self, size, board):
        color = light_blue
        self.x_offset = -0.5
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 4, 0),
            Block(self.color, 5, 0),
            Block(self.color, 6, 0)
        ], dtype=object)
        self.check_lost(board)

    def rotate(self, setup):
        """By pressing the space button, the player can rotate the tetromino"""
        if self.rotating_state == 0:
            if 0 <= self.squares[0].x + 2 <= 9 and 0 <= self.squares[1].x + 1 <= 9 and 0 <= self.squares[
                    3].x - 1 <= 9 and 0 <= self.squares[0].y - 1 < 22 and 0 <= self.squares[
                    2].y + 1 < 22 and 0 <= self.squares[3].y + 2 < 22:
                if not setup[self.squares[0].y - 1][self.squares[0].x + 2] and not setup[self.squares[2].y + 1][
                        self.squares[2].x] and not setup[self.squares[1].y][self.squares[1].x + 1] and not setup[
                        self.squares[3].y + 2][self.squares[3].x - 1]:
                    self.rotating_state = 1
                    self.squares[0].x += 2
                    self.squares[0].y -= 1
                    self.squares[1].x += 1
                    self.squares[2].y += 1
                    self.squares[3].x -= 1
                    self.squares[3].y += 2
        elif self.rotating_state == 1:
            if 0 <= self.squares[0].x - 2 <= 9 and 0 <= self.squares[1].x - 1 <= 9 and 0 <= self.squares[
                    3].x + 1 <= 9 and 0 <= self.squares[0].y + 2 < 22 and 0 <= self.squares[
                    1].y + 1 < 22 and 0 <= self.squares[3].y - 1 < 22:
                if not setup[self.squares[0].y + 2][self.squares[0].x - 2] and not setup[self.squares[1].y + 1][
                        self.squares[1].x - 1] and not setup[
                        self.squares[3].y - 1][self.squares[3].x + 1]:
                    self.rotating_state = 2
                    self.squares[0].x -= 2
                    self.squares[0].y += 2
                    self.squares[1].x -= 1
                    self.squares[1].y += 1
                    self.squares[3].x += 1
                    self.squares[3].y -= 1
        elif self.rotating_state == 2:
            if self.squares[0].x + 1 <= 9 and 0 <= self.squares[2].x - 1 <= 9 and 0 <= self.squares[
                    3].x - 2 <= 9 and 0 <= self.squares[0].y + 1 < 22 and 0 <= self.squares[
                    2].y - 1 < 22 and 0 <= self.squares[3].y - 2 < 22:
                if not setup[self.squares[0].y + 1][self.squares[0].x + 1] and not setup[self.squares[2].y - 1][
                        self.squares[2].x - 1] and not setup[
                        self.squares[3].y - 2][self.squares[3].x - 2]:
                    self.rotating_state = 3
                    self.squares[0].x += 1
                    self.squares[0].y += 1
                    self.squares[2].x -= 1
                    self.squares[2].y -= 1
                    self.squares[3].x -= 2
                    self.squares[3].y -= 2
        elif 0 <= self.squares[0].x - 1 <= 9 and 0 <= self.squares[2].x + 1 <= 9 and 0 <= self.squares[
                3].x + 2 <= 9 and 0 <= self.squares[0].y - 2 < 22 and 0 <= self.squares[
                1].y - 1 < 22 and 0 <= self.squares[3].y + 1 < 22:
            if not setup[self.squares[0].y - 2][self.squares[0].x - 1] and not setup[self.squares[1].y - 1][
                    self.squares[1].x] and not setup[self.squares[2].y][self.squares[2].x + 1] and not setup[
                    self.squares[3].y + 1][self.squares[3].x + 2]:
                self.rotating_state = 0
                self.squares[0].x -= 1
                self.squares[0].y -= 2
                self.squares[1].y -= 1
                self.squares[2].x += 1
                self.squares[3].x += 2
                self.squares[3].y += 1

    def reset(self):
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 4, 0),
            Block(self.color, 5, 0),
            Block(self.color, 6, 0)
        ], dtype=object)
        self.rotating_state = 0


class Square(Tetromino):
    """The yellow tetromino"""

    def __init__(self, size, board):
        color = yellow
        self.x_offset = 0.5
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 4, 0),
            Block(self.color, 5, 0),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.check_lost(board)

    def reset(self):
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 4, 0),
            Block(self.color, 3, 1),
            Block(self.color, 4, 1)
        ], dtype=object)
        self.rotating_state = 0


class T(Tetromino):
    """The purple tetromino"""

    def __init__(self, size, board):
        color = purple
        self.x_offset = 0
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 4, 0),
            Block(self.color, 3, 1),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.check_lost(board)

    def rotate(self, setup):
        """By pressing the space button, the player can rotate the tetromino"""
        if self.rotating_state == 0:
            if self.squares[1].x + 1 <= 9 and self.squares[1].y + 1 < 22:
                if not setup[self.squares[1].y + 1][self.squares[1].x + 1]:
                    self.rotating_state = 1
                    self.squares[1].x += 1
                    self.squares[1].y += 1
        elif self.rotating_state == 1:
            if self.squares[0].x - 1 >= 0 and self.squares[0].y + 1 < 22:
                if not setup[self.squares[0].y + 1][self.squares[0].x - 1]:
                    self.rotating_state = 2
                    self.squares[0].x -= 1
                    self.squares[0].y += 1

        elif self.rotating_state == 2:
            if self.squares[3].x - 1 >= 0 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[3].y - 1][self.squares[3].x - 1]:
                    self.rotating_state = 3
                    self.squares[3].x -= 1
                    self.squares[3].y -= 1
        elif self.squares[0].x + 1 <= 9 and 9 >= self.squares[1].x - 1 >= 0 and self.squares[
                3].x + 1 <= 9 and self.squares[0].y - 1 < 22 and self.squares[1].y - 1 < 22 and self.squares[
                3].y + 1 > 0:
            if not setup[self.squares[0].y - 1][self.squares[0].x + 1] and not setup[self.squares[1].y - 1][
                    self.squares[1].x - 1] and not setup[self.squares[3].y + 1][self.squares[3].x + 1]:
                self.rotating_state = 0
                self.squares[0].x += 1
                self.squares[0].y -= 1
                self.squares[1].x -= 1
                self.squares[1].y -= 1
                self.squares[3].x += 1
                self.squares[3].y += 1

    def reset(self):
        self.squares = np.array([
            Block(self.color, 4, 0),
            Block(self.color, 3, 1),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.rotating_state = 0


class J(Tetromino):
    """The dark blue tetromino"""

    def __init__(self, size, board):
        color = dark_blue
        self.x_offset = 0
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 3, 1),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.check_lost(board)

    def rotate(self, setup):
        """By pressing the space button, the player can rotate the tetromino"""
        if self.rotating_state == 0:
            if self.squares[0].x + 2 < 10 and self.squares[1].x + 1 < 10 and self.squares[
                    3].x - 1 < 10 and self.squares[1].y - 1 >= 0 and self.squares[3].y + 1 < 22:
                if not setup[self.squares[0].y][self.squares[0].x + 2] and not setup[self.squares[1].y - 1][
                        self.squares[1].x + 1] and not setup[self.squares[3].y + 1][self.squares[3].x - 1]:
                    self.rotating_state = 1
                    self.squares[0].x += 2
                    self.squares[1].x += 1
                    self.squares[1].y -= 1
                    self.squares[3].x -= 1
                    self.squares[3].y += 1
        elif self.rotating_state == 1:
            if self.squares[1].x + 1 < 10 and self.squares[3].x - 1 >= 0 and self.squares[
                    0].y + 2 < 22 and self.squares[1].y + 1 < 22 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[0].y + 2][self.squares[0].x] and not setup[self.squares[1].y - 1][
                        self.squares[1].x + 1] and not setup[self.squares[3].y + 1][self.squares[3].x - 1]:
                    self.rotating_state = 2
                    self.squares[0].y += 2
                    self.squares[1].x += 1
                    self.squares[1].y += 1
                    self.squares[3].x -= 1
                    self.squares[3].y -= 1
        elif self.rotating_state == 2:
            if self.squares[0].x - 2 >= 0 and self.squares[1].x - 1 >= 0 and self.squares[
                    3].x + 1 < 10 and self.squares[1].y + 1 < 22 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[0].y][self.squares[0].x - 2] and not setup[self.squares[1].y + 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y - 1][self.squares[3].x + 1]:
                    self.rotating_state = 3
                    self.squares[0].x -= 2
                    self.squares[1].x -= 1
                    self.squares[1].y += 1
                    self.squares[3].x += 1
                    self.squares[3].y -= 1
        elif self.squares[1].x - 1 >= 0 and self.squares[3].x + 1 < 10 and self.squares[0].y - 2 >= 0 and self.squares[
                1].y - 1 >= 0 and self.squares[3].y + 1 < 22:
            if not setup[self.squares[0].y - 2][self.squares[0].x] and not setup[self.squares[1].y - 1][
                    self.squares[1].x - 1] and not setup[self.squares[3].y + 1][self.squares[3].x + 1]:
                self.rotating_state = 0
                self.squares[0].y -= 2
                self.squares[1].x -= 1
                self.squares[1].y -= 1
                self.squares[3].x += 1
                self.squares[3].y += 1

    def reset(self):
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 3, 1),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.rotating_state = 0


class L(Tetromino):
    """The orange tetromino"""

    def __init__(self, size, board):
        color = orange
        self.x_offset = 0
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 5, 0),
            Block(self.color, 5, 1),
            Block(self.color, 4, 1),
            Block(self.color, 3, 1)
        ], dtype=object)
        self.check_lost(board)

    def rotate(self, setup):
        """By pressing the space button, the player can rotate the tetromino"""
        if self.rotating_state == 0:
            if self.squares[1].x - 1 >= 0 and self.squares[3].x + 1 < 10 and self.squares[
                    0].y + 2 < 22 and self.squares[1].y + 1 < 22 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[0].y + 2][self.squares[0].x] and not setup[self.squares[1].y + 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y - 1][self.squares[3].x + 1]:
                    self.rotating_state = 1
                    self.squares[0].y += 2
                    self.squares[1].x -= 1
                    self.squares[1].y += 1
                    self.squares[3].x += 1
                    self.squares[3].y -= 1
        elif self.rotating_state == 1:
            if self.squares[0].x - 2 >= 0 and self.squares[1].x - 1 >= 0 and self.squares[
                    3].x + 1 < 10 and self.squares[1].y - 1 >= 0 and self.squares[3].y + 1 < 22:
                if not setup[self.squares[0].y][self.squares[0].x - 2] and not setup[self.squares[1].y - 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y + 1][self.squares[3].x + 1]:
                    self.rotating_state = 2
                    self.squares[0].x -= 2
                    self.squares[1].x -= 1
                    self.squares[1].y -= 1
                    self.squares[3].x += 1
                    self.squares[3].y += 1
        elif self.rotating_state == 2:
            if self.squares[1].x + 1 < 10 and self.squares[3].x - 1 >= 0 and self.squares[
                    0].y - 2 >= 0 and self.squares[1].y - 1 >= 0 and self.squares[3].y + 1 < 22:
                if not setup[self.squares[0].y - 2][self.squares[0].x] and not setup[self.squares[1].y - 1][
                        self.squares[1].x + 1] and not setup[self.squares[3].y + 1][self.squares[3].x - 1]:
                    self.rotating_state = 3
                    self.squares[0].y -= 2
                    self.squares[1].x += 1
                    self.squares[1].y -= 1
                    self.squares[3].x -= 1
                    self.squares[3].y += 1
        elif self.squares[0].x + 2 < 10 and self.squares[1].x + 1 < 10 and self.squares[3].x - 1 >= 0 and self.squares[
                1].y + 1 < 22 and self.squares[3].y - 1 >= 0:
            if not setup[self.squares[0].y][self.squares[0].x + 2] and not setup[self.squares[1].y + 1][
                    self.squares[1].x + 1] and not setup[self.squares[3].y - 1][self.squares[3].x - 1]:
                self.rotating_state = 0
                self.squares[0].x += 2
                self.squares[1].x += 1
                self.squares[1].y += 1
                self.squares[3].x -= 1
                self.squares[3].y -= 1

    def reset(self):
        self.squares = np.array([
            Block(self.color, 5, 0),
            Block(self.color, 5, 1),
            Block(self.color, 4, 1),
            Block(self.color, 3, 1)
        ], dtype=object)
        self.rotating_state = 0


class S(Tetromino):
    """The green tetromino"""

    def __init__(self, size, board):
        color = green
        self.x_offset = 0
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 5, 0),
            Block(self.color, 4, 0),
            Block(self.color, 4, 1),
            Block(self.color, 3, 1)
        ], dtype=object)
        self.check_lost(board)

    def rotate(self, setup):
        """By pressing the space button, the player can rotate the tetromino"""
        if self.rotating_state == 0:
            if self.squares[1].x + 1 < 10 and self.squares[3].x + 1 < 10 and self.squares[
                    0].y + 2 < 22 and self.squares[1].y + 1 < 22 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[0].y + 2][self.squares[0].x] and not setup[self.squares[1].y + 1][
                        self.squares[1].x + 1] and not setup[self.squares[3].y - 1][self.squares[3].x + 1]:
                    self.rotating_state = 1
                    self.squares[0].y += 2
                    self.squares[1].x += 1
                    self.squares[1].y += 1
                    self.squares[3].x += 1
                    self.squares[3].y -= 1
        elif self.rotating_state == 1:
            if self.squares[0].x - 2 >= 0 and self.squares[1].x - 1 >= 0 and self.squares[
                    3].x + 1 < 10 and self.squares[1].y + 1 < 22 and self.squares[3].y + 1 < 22:
                if not setup[self.squares[0].y][self.squares[0].x - 2] and not setup[self.squares[1].y + 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y + 1][self.squares[3].x + 1]:
                    self.rotating_state = 2
                    self.squares[0].x -= 2
                    self.squares[1].x -= 1
                    self.squares[1].y += 1
                    self.squares[3].x += 1
                    self.squares[3].y += 1
        elif self.rotating_state == 2:
            if self.squares[1].x - 1 >= 0 and self.squares[3].x - 1 >= 0 and self.squares[
                    0].y - 2 >= 0 and self.squares[1].y - 1 >= 0 and self.squares[3].y + 1 >= 0:
                if not setup[self.squares[0].y - 2][self.squares[0].x] and not setup[self.squares[1].y - 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y + 1][self.squares[3].x - 1]:
                    self.rotating_state = 3
                    self.squares[0].y -= 2
                    self.squares[1].x -= 1
                    self.squares[1].y -= 1
                    self.squares[3].x -= 1
                    self.squares[3].y += 1
        elif self.squares[0].x + 2 < 10 and self.squares[1].x + 1 < 10 and self.squares[3].x - 1 >= 0 and self.squares[
                1].y - 1 >= 0 and self.squares[3].y - 1 >= 0:
            if not setup[self.squares[0].y][self.squares[0].x + 2] and not setup[self.squares[1].y - 1][
                    self.squares[1].x + 1] and not setup[self.squares[3].y - 1][self.squares[3].x - 1]:
                self.rotating_state = 0
                self.squares[0].x += 2
                self.squares[1].x += 1
                self.squares[1].y -= 1
                self.squares[3].x -= 1
                self.squares[3].y -= 1

    def reset(self):
        self.squares = np.array([
            Block(self.color, 5, 0),
            Block(self.color, 4, 0),
            Block(self.color, 4, 1),
            Block(self.color, 3, 1)
        ], dtype=object)
        self.rotating_state = 0


class Z(Tetromino):
    """The red tetromino"""

    def __init__(self, size, board):
        color = red
        self.x_offset = 0
        super().__init__(color, size, self.x_offset)
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 4, 0),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.check_lost(board)

    def rotate(self, setup):
        """By pressing the space button, the player can rotate the tetromino"""
        if self.rotating_state == 0:
            if self.squares[0].x + 2 < 10 and self.squares[1].x + 1 < 10 and self.squares[
                    3].x - 1 >= 0 and self.squares[1].y + 1 < 22 and self.squares[3].y + 1 < 22:
                if not setup[self.squares[0].y][self.squares[0].x + 2] and not setup[self.squares[1].y + 1][
                        self.squares[1].x + 1] and not setup[self.squares[3].y + 1][self.squares[3].x - 1]:
                    self.rotating_state = 1
                    self.squares[0].x += 2
                    self.squares[1].x += 1
                    self.squares[1].y += 1
                    self.squares[3].x -= 1
                    self.squares[3].y += 1
        elif self.rotating_state == 1:
            if self.squares[1].x - 1 >= 0 and self.squares[3].x - 1 >= 0 and self.squares[
                    0].y + 2 < 22 and self.squares[1].y + 1 < 22 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[0].y + 2][self.squares[0].x] and not setup[self.squares[1].y + 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y - 1][self.squares[3].x - 1]:
                    self.rotating_state = 2
                    self.squares[0].y += 2
                    self.squares[1].x -= 1
                    self.squares[1].y += 1
                    self.squares[3].x -= 1
                    self.squares[3].y -= 1
        elif self.rotating_state == 2:
            if self.squares[0].x - 2 >= 0 and self.squares[1].x - 1 >= 0 and self.squares[
                    3].x + 1 < 10 and self.squares[1].y - 1 >= 0 and self.squares[3].y - 1 >= 0:
                if not setup[self.squares[0].y][self.squares[0].x - 2] and not setup[self.squares[1].y - 1][
                        self.squares[1].x - 1] and not setup[self.squares[3].y - 1][self.squares[3].x + 1]:
                    self.rotating_state = 3
                    self.squares[0].x -= 2
                    self.squares[1].x -= 1
                    self.squares[1].y -= 1
                    self.squares[3].x += 1
                    self.squares[3].y -= 1
        elif self.squares[1].x + 1 < 10 and self.squares[3].x + 1 < 10 and self.squares[0].y - 2 >= 0 and self.squares[
                1].y - 1 >= 0 and self.squares[3].y + 1 < 22:
            if not setup[self.squares[0].y - 2][self.squares[0].x] and not setup[self.squares[1].y - 1][
                    self.squares[1].x + 1] and not setup[self.squares[3].y + 1][self.squares[3].x + 1]:
                self.rotating_state = 0
                self.squares[0].y -= 2
                self.squares[1].x += 1
                self.squares[1].y -= 1
                self.squares[3].x += 1
                self.squares[3].y += 1

    def reset(self):
        self.squares = np.array([
            Block(self.color, 3, 0),
            Block(self.color, 4, 0),
            Block(self.color, 4, 1),
            Block(self.color, 5, 1)
        ], dtype=object)
        self.rotating_state = 0
