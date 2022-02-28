'''
Eric Hsu Shanker Ram
Snapshot #1: Finished whole wordle game besides settings, + made a word search, hoping to merge the games in the future uwu
Snapshot #2: A lot of gui updates & small changes to wordsearch, split the game into 2 modes: classic / word search, made separate guis for each mode uwu
Snapshot #3: Gui of regular wordle done, almost finished wordsearch wordle, + settings and switching are WIP
'''

from tkinter import *

from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from gui import Screen

# markGuess - will "mark" the guess and the alphabet according to the word
def markGuess(word, guess, alphabet):
    s = guess.getWord()
    mark = [False] * len(word) # is the character from target word used?
    mark2 = [False] * len(s) # is the character from guess used?
    # First iteration - mark correct words
    for i,v in enumerate(s):
        if i < len(word) and word[i] == v:
            mark[i] = True
            mark2[i] = True
            guess.setCorrect(i)
            alphabet.setCorrect(alphabet.getWord().index(v))
    # Second iteration - mark misplaced words
    for i,v in enumerate(s):
        for i2, v2 in enumerate(word):
            if mark2[i]:
                continue
            if mark[i2]:
                continue
            if v == v2:
                mark[i2] = True
                mark2[i] = True
                guess.setMisplaced(i)
                if not alphabet.isCorrect(alphabet.getWord().index(v)):
                    alphabet.setMisplaced(alphabet.getWord().index(v))
    #Third iteration - mark the rest as unused
    for i,v in enumerate(s):
        if not mark2[i]:
            guess.setNotUsed(i)
            if alphabet.colorAt(alphabet.getWord().index(v)):
               alphabet.setColorAt(alphabet.getWord().index(v), "blue")
    return word == s 

# playRound - plays one round of Wordle. 
def playRound(player, words, all_words, settings):
        alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
        word = words.getRandom()
        window = Tk()
        canvas = Canvas(width = 1000, height = 600, bg = "black")

        screen = Screen(canvas, window, False, word, 6)
        print(screen.getGuess())
        if screen.getGuess() == -1: # too many guesses
            print("Sorry, you couldn't find the correct word!")
            print("The word was: " + word)
            print("\n")
            player.updateStats(False, -1)
        else:
            print(screen.getGuess())
            print("Good job, you figured out the word")
            print("\n")
            player.updateStats(True, screen.getGuess())
        player.displayStats()


def playWordle():
    print("Let's play the game of Wordle!!")
    name = input("Enter your name: ")
    print("Welcome " + name + "!\n")
    print("OK, let's play Wordle!!\n")

    # initialize WordBanks
    common5letter = WordBank("common5letter.txt")
    all_words = WordBank("words_alpha.txt")

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # make the player
    player = WordlePlayer(name)

    tmp2 = True
    while tmp2:
        playRound(player, common5letter, all_words, settings)
        playAgain = input("Did you want to play again? (y/n): ").lower()
        print("\n")
        if not (playAgain == "yes" or playAgain == "y"):
            tmp2 = False
    
    print("\n")
    player.displayStats()
    print("\n")
    print("Bye! It was good playing Wordle with you!")
            

def main():
    playWordle()

if __name__ == "__main__":
    main()