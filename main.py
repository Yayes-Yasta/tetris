"""This is the file that should be executed in order to start playing Tetris"""
import os
import time
import sys

import numpy as np
import pygame

from classes.game import Game


def main(height=500):
    """This is the main function that gets executed when this file is run"""
    # initialization
    pygame.init()
    pygame.joystick.init()
    # variables
    square_size = height // 22
    icon = pygame.image.load(os.path.join('images', 'icon.png'))
    window = pygame.display.set_mode((height, height))
    pygame.display.set_caption('Tetris')
    pygame.display.set_icon(icon)
    run = True
    board = Game(height)
    clock = pygame.time.Clock()
    next_drop = time.time() + 1
    time_difference = 1
    font = pygame.font.SysFont('comicsans', height // 20)
    # controller input
    joysticks = np.empty(0, dtype=object)
    for i in range(pygame.joystick.get_count()):
        joysticks = np.append(joysticks, [pygame.joystick.Joystick(i)])
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            # keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.dropping.rotate(board.setup)

                elif event.key == pygame.K_LEFT:
                    board.left()

                elif event.key == pygame.K_UP:
                    board.up()

                elif event.key == pygame.K_RIGHT:
                    board.right()

                elif event.key == pygame.K_DOWN:
                    board.down()
                    next_drop = time.time() + time_difference

                elif event.key == pygame.K_c:
                    board.switch()
            # controller input
            elif event.type == pygame.JOYBUTTONDOWN:
                # UP
                if event.button == 11:
                    board.up()
                # DOWN
                elif event.button == 12:
                    board.down()
                    next_drop = time.time() + time_difference
                # LEFT
                elif event.button == 13:
                    board.left()
                # RIGHT
                elif event.button == 14:
                    board.right()
                # Playstation: X; Xbox: A
                elif event.button == 0:
                    board.dropping.rotate(board.setup)
                # Playstation: L1; Xbox: LB
                elif event.button == 9:
                    board.switch()
            elif event.type == pygame.QUIT:
                run = False
                break

        board.draw(window, height, square_size, font)
        current_time = time.time()
        if current_time >= next_drop:
            next_drop += time_difference
            time_difference -= 0.000001
            if board.dropping:
                board.drop()
            else:
                board.start_drop()

    pygame.display.quit()
    pygame.joystick.quit()
    quit()
    print("End reached")
    sys.exit()


if __name__ == '__main__':
    main()
