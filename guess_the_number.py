#!/usr/bin/env python
# coding: utf-8

import random


# Below function is play to guess the random number that is generated by computer.
def guess(x):
    
    random_number = random.randint(1,x)
    guess = 0
    
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x} :  "))
        
        if(guess < random_number):
            print('Sorry, guess again. Too low.')
        else:
            print('Sorry, guess again. Too high.')
    
    print(f'\nYay, Congrats, you have guessed the number, {random_number}')


# Below function is game if computer identifies the random number generated by us.
def guess_computer(x):
    
    low = 1
    high = x
    
    feedback = ''
    
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is the guess, {guess} is high(H), low (L) or correct(C) ??').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay, the computer guessed the number, {guess} correctly!')
