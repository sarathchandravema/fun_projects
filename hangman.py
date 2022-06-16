#!/usr/bin/env python
# coding: utf-8

from words import words

import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words).upper()
    letters_in_word = set(word)
    alphabs = set(string.ascii_uppercase)
    guessed_letters = set()
    lives = 6
    
    while len(letters_in_word) > 0 and lives != 0:
        print('\n')
        
        print(f'You have {lives} lives left.')
        #printing guessed letters 
        print('Letters you\'ve guessed ', ' '.join(guessed_letters))
        
        #current word
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Guessed word:  ',' '.join(word_list))
        
        #guessed user input
        user_letter = input("Guess a letter :   ").upper()
        if user_letter in alphabs - guessed_letters :
            guessed_letters.add(user_letter)
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')
        elif user_letter in guessed_letters:
            print('This letter is already guessed.')
        else:
            print('It is an invalid character. Please provide inputs in a-z')
    
    print('\n')
    if lives == 0:
        print(f'Sorry, you are dead and the word is {word}')
    else:
        print(f'Yay..!! You\'ve guessed the word correctly {word}')

if __name__ == '__main__':
    hangman()