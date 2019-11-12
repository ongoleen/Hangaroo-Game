# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random
import string

WORDLIST_FILENAME = "words.txt"
wordlist = ["pikachu","pokemon","sad","lost","hanged","nails","fall","stop","stop","couch","soil","rock","python","anaconda","snake","piano","harp","power","gosh",]

def loadWords():
    print("Loading...")
    print("  ", len(wordlist), " words. Loading Complete.")
    return wordlist
def chooseWord(wordlist):
    return random.choice(wordlist)
secretWord = chooseWord(wordlist)

def chooseWord(wordlist):
      return (random.choice(wordlist))

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
  
def Hangaroo(secretWord):    
    numletters = len(secretWord)
    lettersGuessed = []
    guess = str
    mistakes = 4
    wordGuessed = False
    
    print("Hey Hooman! Ready to Hang some Kangaroos?")
    print("The word to guess is ", numletters, " letters long.")
    print('------------')
    while mistakes > 0 and mistakes <= 4 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ("You have ",mistakes ," guesses left.")
        print ('Available letters: ',getAvailableLetters(lettersGuessed))
        guess = input('Guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Stop Hooman you guessed that already: ",getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ("Nice one Hooman: ",getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Stop Hooman you guessed that already: ",getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakes -= 1
                print ("Think Hooman that Letter not Here: ", getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
    
    if wordGuessed == True:
        print("'That's my Hooman! Doge Labs You'")
    elif mistakes == 0:
        print ('Try Again Next Time My Favorite Hooman. The Word was ',secretWord)