import pygame
import sys
import numpy as np
import random

pygame.init()
Length = 900
Width = 900
screen_color = (116, 247, 243)
line_color = (81, 148, 237)
circle_color = (200, 135, 89)
cross_color = (61, 20, 1)
b_rows = 3
b_colms = 3

screen = pygame.display.set_mode((Width, Length))
pygame.display.set_caption("TIC TAC TOE by shubham")
screen.fill(screen_color)
square_size = 300
line_width = 10
circle_size = 300
circle_radius = 75
circle_width = 15
cross_size = 300
cross_space = 75
cross_width = 15

anyPlayer = random.randint(1, 2)


def draw_figs():
    for rows in range(b_rows):
        for colms in range(b_colms):
            if g_board[rows][colms] == 1:
                pygame.draw.circle(screen, circle_color, (
                    int(colms * circle_size + circle_size // 2), int(rows * circle_size + circle_size // 2)), circle_radius,
                    circle_width)
            elif g_board[rows][colms] == 2:
                pygame.draw.line(screen, cross_color,
                                 (colms * cross_size + cross_space, rows *
                                  cross_size + cross_size - cross_space),
                                 (colms * cross_size + cross_size -
                                  cross_space, rows * cross_size + cross_space),
                                 cross_width)
                pygame.draw.line(screen, cross_color,
                                 (colms * cross_size + cross_space, rows * cross_size + cross_space), (
                                     colms * cross_size + cross_size - cross_space,
                                     rows * cross_size + cross_size - cross_space), cross_width)


def draw_lines():
    pygame.draw.line(screen, line_color, [0, 300], [900, 300], 10)
    pygame.draw.line(screen, line_color, [0, 600], [900, 600], 10)
    pygame.draw.line(screen, line_color, [300, 0], [300, 900], 10)
    pygame.draw.line(screen, line_color, [600, 0], [600, 900], 10)


def mark_sqaure(rows, colms, player):
    g_board[rows][colms] = player


def available_space(rows, colms):
    return g_board[rows][colms] == 0


def full_board():
    for rows in range(b_rows):
        for colms in range(b_colms):
            if g_board[rows][colms] == 0:
                return False
    return True


def who_win(player):
    # vertically wins
    for colms in range(b_colms):
        if g_board[0][colms] == player and g_board[1][colms] == player and g_board[2][colms] == player:
            draw_vertical_line(colms, player)
            return True

    for rows in range(b_rows):
        if g_board[rows][0] == player and g_board[rows][1] == player and g_board[rows][2] == player:
            draw_horizontal_line(rows, player)
            return True

    if g_board[0][0] == player and g_board[1][1] == player and g_board[2][2] == player:
        draw_digonal_1(player)
        return True

    elif g_board[2][0] == player and g_board[1][1] == player and g_board[0][2] == player:
        draw_digonal_2(player)
        return True


def draw_vertical_line(colms, player):
    posX = colms * square_size + square_size // 2
    if player == 1:
        line_color = circle_color
    elif player == 2:
        line_color = cross_color

    pygame.draw.line(screen, line_color, (posX, 20),
                     (posX, Length - 20), line_width)


def draw_horizontal_line(rows, player):
    posY = rows * square_size + square_size // 2
    if player == 1:
        line_color = circle_color
    elif player == 2:
        line_color = cross_color

    pygame.draw.line(screen, line_color, (20, posY),
                     (Width - 20, posY), line_width)


def draw_digonal_1(player):
    if player == 1:
        line_color = circle_color
    elif player == 2:
        line_color = cross_color

    pygame.draw.line(screen, line_color, (20, 20),
                     (Width - 20, Length - 20), line_width)


def draw_digonal_2(player):
    if player == 1:
        line_color = circle_color
    elif player == 2:
        line_color = cross_color

    pygame.draw.line(screen, line_color, (Length - 20, 20),
                     (20, Width - 20), line_width)


def restart_game():
    screen.fill(screen_color)
    draw_lines()
    for rows in range(b_rows):
        for colms in range(b_colms):
            g_board[rows][colms] = 0


draw_lines()

g_board = np.zeros((b_rows, b_colms))
player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 300)
            clicked_colm = int(mouseX // 300)

            if available_space(clicked_row, clicked_colm):
                mark_sqaure(clicked_row, clicked_colm, player)
                if player == 1:
                    mark_sqaure(clicked_row, clicked_colm, 1)
                    if who_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_sqaure(clicked_row, clicked_colm, 2)
                    if who_win(player):
                        game_over = True
                    player = 1
            draw_figs()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart_game()
                player = 2
                game_over = False

    # pygame.display.update()
    pygame.display.flip()
