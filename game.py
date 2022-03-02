'''
Eric Hsu Shanker Ram
Snapshot #1: Finished whole wordle game besides settings, + made a word search, hoping to merge the games in the future uwu
Snapshot #2: A lot of gui updates & small changes to wordsearch, split the game into 2 modes: classic / word search, made separate guis for each mode uwu
Snapshot #3: Gui of regular wordle done, almost finished wordsearch wordle, + settings and switching are WIP
Snapshot #4: Everything pretty much done, just need to compile it together, + added confetti ;)
'''

from tkinter import *

from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from gui import Screen
from actualgame import actualgame

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
            #guess.setNotUsed(i)
            #guess.setColorAt(i, "blue")
            if not alphabet.isCorrect(alphabet.getWord().index(v)) and not alphabet.isMisplaced(alphabet.getWord().index(v)):
                alphabet.setNotUsed(alphabet.getWord().index(v))
            #if alphabet.colorAt(alphabet.getWord().index(v)):
            #alphabet.setColorAt(alphabet.getWord().index(v), "blue")
    #return word == s 

# playRound - plays one round of Wordle. 
def playRound(player, words, all_words, settings):
    alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
    word = words.getRandom()

    if True:
        won = False
        cnt = 1
        guesses = []
        while not won and cnt <= settings.getValue('maxguess'):
            guess = input("Enter a 5-letter guess: ")
            if guess == "quit": # quit
                cnt = settings.getValue('maxguess')+1 # a little hack ;)
                break
            if not all_words.contains(guess) or len(guess) != 5: #invalid word
                print("'" + guess + "' needs to be a 5-letter valid word")
                continue
            guess = WordleWord(guess)
            won = markGuess(word, guess, alphabet)
            guesses.append(guess)
            print("\n")
            for i,v in enumerate(guesses):
                print(str(i+1)+": "+str(v))
            print("\n"+str(alphabet)+"\n")
            won = guess.getWord() == word
            if not won:
                cnt += 1
        if cnt == settings.getValue('maxguess')+1: # too many guesses
            print("Sorry, you couldn't find the correct word!")
            print()
            print("The word was: " + word)
            print()
            player.updateStats(False, -1)
        else:
            print("Good job, you figured out the word")
            print()
            player.updateStats(True, cnt)
            


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
    player = WordlePlayer(name, 6)

    stillplaying = True
    while stillplaying:
        playRound(player, common5letter, all_words, settings)
        playAgain = input("Did you want to play again? (y/n): ").lower()
        if not (playAgain == "yes" or playAgain == "y"):
            stillplaying = False
    
    print("Bye! It was good playing Wordle with you!") 
    print()
    player.displayStats()

def main():
    answer = input("Are you a robot??").lower()
    if answer == 'y' or answer == 'yes':
        playWordle()
    else:
        actualgame()

player = WordlePlayer("mark",6)
player.updateStats(1,2)
player.displayStats()
player.updateStats(0,69)
player.displayStats()
if __name__ == "__main__":
    main()