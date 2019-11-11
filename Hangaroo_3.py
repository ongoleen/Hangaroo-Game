# -*- coding: utf-8 -*-
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
import string
def getAvailableLetters(lettersGuessed):
      alphabets = string.ascii_lowercase
      for letter in lettersGuessed:
        if letter in alphabets:
            alphabets = alphabets.replace(letter, '')
      return alphabets
print (getAvailableLetters(lettersGuessed))