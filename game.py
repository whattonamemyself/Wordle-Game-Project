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
def playRound(player, words, all_words, settings):
    
        uwu = WordleGame(words.getRandom())
        tmp = True
        cnt = 1
        while tmp and cnt <= settings.getValue('maxguess'):
            print("Enter a 5 letter word")
            guess = input()
            if guess == "quit":
                cnt = settings.getValue('maxguess')+1
                break
            if not all_words.contains(guess) or len(guess) != 5:
                print("Enter a valid word")
                continue
            x = uwu.guess(guess)
            print(x[1])
            tmp = not x[0]
            if tmp:
                print(uwu.getAlphabet())
            if tmp:
                cnt += 1
        if cnt == settings.getValue('maxguess')+1:
            print("YOU LOSE")
            print("The word was:" + uwu.getWordleWord())
            player.updateStats(False, -1)
        else:
            print("YOU WIN")
            player.updateStats(True, cnt)
        player.displayStats()


def playWordle():
    print("Let's play the game of Wordle!")

    print("What is your name?")
    name = input()

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
        print("Play again? y / n")
        asdf = input().lower()
        if not (asdf == "yes" or asdf == "y"):
            tmp2 = False
    
    print("Thanks for Playing Wordle!!")
    player.displayStats()
            

def main():
    playWordle()

if __name__ == "__main__":
    main()