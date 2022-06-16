#!/usr/bin/env python
# coding: utf-8

import random

def play():
    """
    Function to play the game , where everyone gives their inputs
    """
    
    user = input('Rock(r) or Paper(p) or Scissors(s) :  ').lower()
    comp = random.choice(['r', 'p', 's'])
    
    if user == comp:
        return 'It\'s a tie!!'
    
    if is_win(user, comp):
        return 'You won the game!!'
    
    return 'You lost.'


# Order of hierarchy to win: r > s, s > p, p > r 

def is_win(player1, player2):
    """
    Function to identify who won the game
    """

    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or     (player1 == 'p' and player2 == 'r'):
            return True        

if __name__ == "__main__":
    play()