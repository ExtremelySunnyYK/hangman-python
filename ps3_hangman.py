# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    a=[]
    for i in secretWord:
        a.append(i)
    return(set(a).issubset(set(lettersGuessed)))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for i in secretWord:
        if i in lettersGuessed:
            ans = ans + i
            
        else:
            ans = ans + '_'
            
    return(' '.join(ans))



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = list(string.ascii_lowercase[:27])
    for i in lettersGuessed:
            if i in alpha:
                alpha.remove(i)          
            else:
                continue
    return(''.join(sorted(alpha)))
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lines = "-----------"
    print(lines)
    lettersGuessed = []
    guesstotal = 8
    
    
    #Loop for each guess. word not guessed yet
    while isWordGuessed(secretWord, lettersGuessed) is False:
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        print("You have "+ str(guesstotal) +" guesses left.")
        typetheletter = input("Please guess a letter: ")
        print(lines)
        lettersGuessed.append(typetheletter)
        
        #guess correct
        
        if typetheletter in secretWord:
            print("Good guess:" + str(getGuessedWord(secretWord, lettersGuessed)))
            print(lines)
                
        #guess wrong
        else:
            print("Oops! That letter is not in my word:" + str(getGuessedWord(secretWord, lettersGuessed)))
            guesstotal = guesstotal - 1
            print(lines)
            print(lettersGuessed)
            
        #if you lose the game
        if guesstotal == 0:
            print("Sorry, you ran out of guesses. The word was " + str(secretWord) +  " .")
            break
            
    #if the word is guessed alr
    else:
        print("Congratulations, you won!")
        print(lettersGuessed)

while True:
    hangman(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
