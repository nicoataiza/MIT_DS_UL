# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return all([let in letters_guessed for let in secret_word])



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return "".join([let if let in letters_guessed else "_ " for let in secret_word])



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    return "".join([let for let in string.ascii_lowercase if let not in letters_guessed])
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    lives = 5
    warnings = 2
    print(f"Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("_ "*len(secret_word))
    print(f"You have {warnings+1} warnings left")
    print("-----------")
    letters_guessed = []
    while lives >= 0 and not(is_word_guessed(secret_word,letters_guessed)):
      print(f"You have {lives + 1} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      # if there is no guess
      guess = input("Please guess a letter: ")
      guess = guess.lower()
      # Check if valid guess
      if not(guess.isalpha()) or (guess in letters_guessed):
        if not(guess.isalpha()):
          text1 = "Oops! That is not a valid letter!"
        elif (guess in letters_guessed):
          text1 = "Oops! You've already guessed that letter."
        if warnings >= 0: 
          text2 = "You have {} warnings left: {}".format(warnings,get_guessed_word(secret_word,letters_guessed))
          warnings -= 1
        else:
          text2 = "You have no warnings left you lose one guess: {}".format(get_guessed_word(secret_word,letters_guessed))
          lives -= 1
        print("{} {} ".format(text1,text2))
        print("-----------")
        continue
          
      letters_guessed.append(guess)
      # if the guess is correct
      if guess in secret_word:
        print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")
      else:
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}")
        if guess in ["a","e","i","o","u"]:
          lives -=2
        else:
          lives -=1
      print("-----------")
      #check if win
    if lives < 0 :
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
      print("Congratulations, you won!")
      print(f"Your total score for this game is: {lives+1*len(letters_guessed)}")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # length
    my_word, other_word = ''.join([let for let in my_word if let != " "]), other_word.strip()
    l = len(my_word) == len(other_word)
    # check if non _ are the same
    c = [a==b for (a,b) in zip(my_word,other_word) if a!="_"]
    # check for _ has the same letters ; so if theyre no th
    d = [b for (a,b) in zip(my_word,other_word) if a=="_"]

    return l and all(c) and not(any([char in my_word for char in d]))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    to_ = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        to_.append(word)
    if len(to_) == 0:
      print("No matches found")
    else:
      print(" ".join(to_))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    lives = 5
    warnings = 2
    print(f"Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("_ "*len(secret_word))
    print(f"You have {warnings+1} warnings left")
    print("-----------")
    letters_guessed = []
    while lives >= 0 and not(is_word_guessed(secret_word,letters_guessed)):
      print(f"You have {lives + 1} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      # if there is no guess
      guess = input("Please guess a letter: ")
      guess = guess.lower()
      # Check if valid guess
      if not(guess.isalpha()) or (guess in letters_guessed):
        if not(guess.isalpha()):
          if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
            print("-----------")
            continue
          text1 = "Oops! That is not a valid letter!"
        elif (guess in letters_guessed):
          text1 = "Oops! You've already guessed that letter."
        if warnings >= 0: 
          text2 = "You have {} warnings left: {}".format(warnings,get_guessed_word(secret_word,letters_guessed))
          warnings -= 1
        else:
          text2 = "You have no warnings left you lose one guess: {}".format(get_guessed_word(secret_word,letters_guessed))
          lives -= 1
        print("{} {} ".format(text1,text2))
        print("-----------")
        continue
          
      letters_guessed.append(guess)
      # if the guess is correct
      if guess in secret_word:
        print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")
      else:
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}")
        if guess in ["a","e","i","o","u"]:
          lives -=2
        else:
          lives -=1
      print("-----------")
      #check if win
    if lives < 0 :
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
      print("Congratulations, you won!")
      print(f"Your total score for this game is: {lives+1*len(letters_guessed)}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
