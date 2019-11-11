# -*- coding: utf-8 -*-
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def getGuessedWord(secretWord, lettersGuessed):
       user_guess = ''
       for letter in secretWord:
        if letter in lettersGuessed:
            user_guess += letter
        else:
            user_guess += '_ '
       return user_guess
print (getGuessedWord(secretWord, lettersGuessed))