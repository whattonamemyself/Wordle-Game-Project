#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# State Attributes
#   - word - String - the word
#   - color - List - a list of strings which indicate the color or each word
#                  - colors: 'normal', 'green', 'yellow', 'red', 'blue' and 'gray' are supported
#
# Methods
#   - getWord() - returns the word
#   - setColor(color) - sets the color of the entire word to 'color'
#   - charAt(pos) - returns the letter of the word at pos
#   - getChColor(pos) - returns the color of the letter at pos
#   - setChColor(pos, color) - sets the color of the letter at pos to color
#   - __str__() - returns an ANSI colored string of the word
#   - __eq__() - compares the word of two Fancy words
#===========================================================================
from fancyword import FancyWord

# TODO - make WordleWord
#hello

class WordleWord(FancyWord):
    def __init__(self, w):
        super().__init__(w)
    def isCorrect(self, pos):
        return super().colorAt(pos) == "green"
    def isMisplaced(self, pos):
        return super().colorAt(pos) == "yellow"
    def isNotUsed(self, pos):
        return super().colorAt(pos) == "gray"
    def setCorrect(self, pos):
        super().setColorAt(pos, "green")
    def setMisplaced(self, pos):
        super().setColorAt(pos, "yellow")
    def setNotUsed(self, pos):
        super().setColorAt(pos, "gray")
    def posOf(self, val):
        return self.word.find(val)
