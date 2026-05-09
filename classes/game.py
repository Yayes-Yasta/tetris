"""The game itself happens here"""
import secrets

import numpy as np
import pygame

from classes.tetrominoes import Square, Straight, S, Z, L, J, T
from colors.colors import LINES, BACKGROUND

tetrominoes = [T, Straight, Square, J, L, Z, S]


class Game:
    """This is the class that represents everything that is happening"""
    def __init__(self, height):
        self.setup = np.empty((22, 10), dtype=object)
        self.height = height
        self.rows = np.zeros(22, dtype=np.uint8)
        self.dropping = self.get_random_tetromino()
        self.next = self.get_random_tetromino()
        self.holding = None
        self.switch_allowed = True

    def draw(self, window, height, square_size, font):
        """The entire window will be drawn here"""
        window.fill(BACKGROUND)
        # squares on the board
        for row in self.setup:
            for square in row:
                if square:
                    square.draw(window, square_size, 0)

        self.dropping.draw(window, square_size)
        x = square_size * 6
        # left line of the board
        pygame.draw.line(window, LINES, (x, 0), (x, height))
        # HOLD section
        pygame.draw.rect(window, LINES, (0, 0, x + 1, x), 1)
        window.blit(font.render('Hold:', True, LINES), (1, 0))
        if self.holding:
            self.holding.draw(window, square_size, 1)
        # right line of the board
        x = square_size * 16
        pygame.draw.line(window, LINES, (x, 0), (x, height))
        # NEXT section
        pygame.draw.rect(window, LINES, (x, 0, height - x, height - x), 1)
        window.blit(font.render('Next:', True, LINES), (x + 1, 0))
        self.next.draw(window, square_size, 2)

        pygame.display.update()

    def start_drop(self):
        """When there is no tetromino, this function will create the next tetromino"""
        self.add_to_rows()
        for block in self.dropping.squares:
            self.setup[block.y][block.x] = block
        self.dropping = self.next
        self.next = self.get_random_tetromino()
        self.full_row()
        self.switch_allowed = True

    def drop(self):
        """Every second, the falling tetromino approaches the ground"""
        for block in self.dropping.squares:
            if block.y >= 21 or self.setup[block.y + 1][block.x]:
                self.start_drop()
                return 0
        self.dropping.drop()

    def left(self):
        for square in self.dropping.squares:
            if square.x - 1 < 0 or self.setup[square.y][square.x - 1]:
                return
        for square in self.dropping.squares:
            square.x -= 1

    def right(self):
        for square in self.dropping.squares:
            if square.x + 1 > 9 or self.setup[square.y][square.x + 1]:
                return
        for square in self.dropping.squares:
            square.x += 1

    def down(self):
        self.drop()

    def up(self):
        while True:
            if self.drop() == 0:
                break

    def full_row(self):
        for row in range(22):
            if self.rows[row] == 10:
                self.rows[row] = 0
                self.setup = np.append([np.empty(10, dtype=object)], np.delete(self.setup, row, axis=0), axis=0)
                self.rows = np.append(0, np.delete(self.rows, row))
                for i in range(row + 1):
                    for j in range(10):
                        if self.setup[i][j]:
                            self.setup[i][j].y += 1

    def add_to_rows(self):
        for square in self.dropping.squares:
            self.rows[square.y] += 1

    def switch(self):
        if self.switch_allowed:
            self.switch_allowed = False
            self.dropping.reset()
            if self.holding:
                self.dropping, self.holding = self.holding, self.dropping
                return
            self.holding = self.dropping
            self.dropping = self.next
            self.next = self.get_random_tetromino()

    def get_random_tetromino(self):
        return secrets.choice(tetrominoes)(self.height // 22, self.setup)
