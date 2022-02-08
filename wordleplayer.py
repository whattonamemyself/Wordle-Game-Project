#===========================================================================
# class WordlePlayere
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
#===========================================================================
# Description: a card player with money and a hand of stack_of_cards
#
# State Attributes
#    name - string - the name of the player
#    score - integer - how many points the player has
# Methods
#    introduce() - prints out message "Hi, my name is ..."
#    __str__() - returns a string ex. 'Joe: 5 points'
#    getName() - returns the name of the player
#===========================================================================
from player import Player

# TODO - make WordlePlayer

class WordlePlayer(Player):
    def __init__(self, n):
        super().__init__(n)
        self.won = 0
        self.games = 0
        self.streak = 0
        self.maxstreak = 0
        self.tries = [0] * 6 # 6 being maximum tries
    def updateStats(self, won, tries):
        if won:
            self.tries[tries - 1] += 1
            self.won += 1
            self.streak += 1
            self.maxstreak = max(self.maxstreak, self.streak)
        else:
            self.streak = 0
        self.games += 1
    def winPercentage(self):
        return self.won / self.games
    def gamesPlayed(self):
        return self.games
    def currentStreak(self):
        return self.streak
    def maxStreak(self):
        return self.maxstreak
    def displayStats(self):
        print("Games Played:", self.gamesPlayed())
        print("Win %:", self.winPercentage())
        print("Current Streak:",self.currentStreak())
        print("Max Streak:", self.maxStreak())
        print("Guess Distribution")
        peak = max(self.tries)
        for i, v in enumerate(self.tries):
            print(str(i+1)+": ", "#"*(v*20//peak + 1))
