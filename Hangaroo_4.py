# -*- coding: utf-8 -*-
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
      print ("Loading word list from file...")
      inFile = open(WORDLIST_FILENAME, 'r', 0)
      line = inFile.readline()
      wordlist = string.split(line)
      print ("  "), len(wordlist), ("words loaded.")
      return wordlist
  
def chooseWord(wordlist):
      return (random.choice(wordlist))

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
       user_guess = ''
       for letter in secretWord:
        if letter in lettersGuessed:
            user_guess += letter
        else:
            user_guess += '_ '
       return user_guess
   
def getAvailableLetters(lettersGuessed):
      alphabets = string.ascii_lowercase
      for letter in lettersGuessed:
        if letter in alphabets:
            alphabets = alphabets.replace(letter, '')
      return alphabets
  
def hangman(secretWord):
     guessesLeft = 8
     lettersGuessed = []
     separator = '-------------'

     print ("Welcome to the game, Hangman!")
     print ("I am thinking of a word that is ") + \
        str(len(secretWord)) + (" letters long.")
     print (separator)

     while guessesLeft > 0:
        print ("You have ") + str(guessesLeft) + (" guesses left.")
        print ("Available letters: ") + getAvailableLetters(lettersGuessed)
        letter = raw_input,("Please guess a letter: ").lower()
        if letter in secretWord:
            if letter in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + \
                    getGuessedWord(secretWord, lettersGuessed)
                print (separator)
            else:
                lettersGuessed.append(letter)
                print ("Good guess: ") + \
                    getGuessedWord(secretWord, lettersGuessed)
                print (separator)
        else:
            if letter in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + \
                    getGuessedWord(secretWord, lettersGuessed)
                print (separator)
            else:
                lettersGuessed.append(letter)
                print ("Oops! That letter is not in my word: ") + \
                    getGuessedWord(secretWord, lettersGuessed)
                guessesLeft -= 1
                print (separator)
        if isWordGuessed(secretWord, lettersGuessed):
            return ("Congratulations, you won!")
        return ("Sorry, you ran out of guesses. The word was else.")