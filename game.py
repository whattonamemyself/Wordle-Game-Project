import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from wordlegame import WordleGame


#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    pass  # TODOa

#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======
def playRound(players, words, all_words, settings):
    pass # TODO


def playWordle():
    print("Let's play the game of Wordle!")

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # make the player
    player = WordlePlayer()

    uwu = WordleGame(all_words.getRandom())
    print(uwu.getWordleWord())
    tmp = True
    while tmp:
        guess = input()
        x = uwu.guess(guess)
        print(x[1])
        tmp = not x[0]
    print("YOU WIN")
    # start playing rounds of Wordle

    # end game by displaying player stats

def main():
    playWordle()

if __name__ == "__main__":
    main()