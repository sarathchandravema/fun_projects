import random
import math


class Player:
    def __init__(self, letter):
        """
        letter is x or o
        :param letter:
        """
        self.letter = letter

    def get_move(self, game):
        """
        all players to get their next move given a game
        :param game: list of available tiles from the game
        :return: one tile from the available tiles
        """
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        tile = random.choice(game.available_moves())
        return tile


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        moves = game.available_moves()
        valid_square = False
        position = None
        while not valid_square:
            tile = input(f"{self.letter}'s turn. Input a position from the available positions, {moves} : ")
            try:
                position = int(tile)
            except ValueError:
                print("Provided input is not an integer")
            if position not in moves:
                raise ValueError("Provide valid position")
            valid_square = True

        return position
