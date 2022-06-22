from game import TicTacToe
from player import HumanPlayer, ComputerPlayer


def play(game, x_player, o_player, print_board=True):
    if print_board:
        game.numbers_for_tiles()

    # game is always started by player with letter 'X'
    letter = 'X'
    while game.any_empty_squares():
        if letter == 'O':
            tile = o_player.get_move(game)
        else:
            tile = x_player.get_move(game)

        # let's make a move
        if game.make_move(tile, letter):
            if print_board:
                print(f"{letter} player makes a move on tile {tile}")
                game.print_board()
                print('\n')

            if game.current_winner:
                if print_board:
                    print(f"{letter} wins the game..!!!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_board:
        print("It's a tie")


if __name__ == '__main__':
    print('Welcome to play Tic-Tac-Toe')
    t_game = TicTacToe()
    player1 = HumanPlayer("X")
    player2 = ComputerPlayer("O")
    play(t_game, player1, player2)
