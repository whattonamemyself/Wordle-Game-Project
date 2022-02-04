import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer

#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    pass  # TODO

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
    ...

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # make the player

    # start playing rounds of Wordle

    # end game by displaying player stats

def main():
    playWordle()

if __name__ == "__main__":
    main()