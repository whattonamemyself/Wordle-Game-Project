'''
Current snapshot: finished basic skeleton of the game, playable but no extra features e.g. settings
'''



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
    s = guess.getWord()
    mark = [False] * len(word)
    mark2 = [False] * len(s)
    for i,v in enumerate(s):
        if i < len(word) and word[i] == v:
            mark[i] = True
            mark2[i] = True
            guess.setCorrect(i)
            alphabet.setCorrect(alphabet.getWord().index(v))
    for i,v in enumerate(s):
        if mark2[i]:
            continue
        for i2, v2 in enumerate(word):
            if mark[i2]:
                continue
            if v == v2:
                mark[i2] = True
                mark2[i] = True
                guess.setMisplaced(i)
                if not alphabet.isCorrect(alphabet.getWord().index(v)):
                    alphabet.setMisplaced(alphabet.getWord().index(v))
    for i,v in enumerate(s):
        if not mark2[i]:
            guess.setNotUsed(i)
            if alphabet.colorAt(alphabet.getWord().index(v)):
               alphabet.setColorAt(alphabet.getWord().index(v), "blue")
    return not word == s

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
        alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
        word = words.getRandom()
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
            guess = WordleWord(guess)
            tmp = markGuess(word, guess, alphabet)
            print(guess)
            if tmp:
                print(alphabet)
                cnt += 1
            
        if cnt == settings.getValue('maxguess')+1:
            print("YOU LOSE")
            print("The word was:" + word)
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