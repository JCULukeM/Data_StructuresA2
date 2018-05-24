""" playgame.py

Contains the Connect 3 game playing application.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""
from connect3board import Connect3Board
from gametree import GameTree


def main():
    print('Welcome to Connect 3 by Luke Maclean')
    mode = get_mode()
    while mode != 'Q':
        if mode == 'A':
            run_two_player_mode()
        elif mode == 'B':
            run_ai_mode()
        mode = get_mode()


def run_two_player_mode():
    game_not_done = True
    board = Connect3Board(3, 3)
    while game_not_done:
        print(board)
        whose_turn = board.get_whose_turn()
        token_choice = int(input("Choose a row to place a {}: ".format(whose_turn)))
        board.add_token(token_choice)
        if board.get_winner() is not None:
            winner = board.get_winner()
            game_not_done = False
            print(board)
            print("Player {} won".format(winner))

    # for you to complete...
    pass


def run_ai_mode():

    # for you to complete...
    pass


def get_mode():
    mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    while mode[0].upper() not in 'ABQ':
        mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    return mode[0].upper()


def get_int(prompt):
    result = 0
    finished = False
    while not finished:
        try:
            result = int(input(prompt))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")
    return result


if __name__ == '__main__':
    main()
