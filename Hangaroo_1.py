secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
print (isWordGuessed(secretWord, lettersGuessed))