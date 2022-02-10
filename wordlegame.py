
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly

# Methods
#   - getWord() - returns the word
#   - setColor(color) - sets the color of the entire word to 'color'
#   - charAt(pos) - returns the letter of the word at pos
#   - getChColor(pos) - returns the color of the letter at pos
#   - setChColor(pos, color) - sets the color of the letter at pos to color
#   - __str__() - returns an ANSI colored string of the word
#   - __eq__() - compares the word of two Fancy words hello eric
from wordleword import WordleWord
class WordleGame():
    def __init__(self, s):
        self.target = s
        self.guesses = []
        self.alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
    def guess(self, s):
        target = self.target
        res = WordleWord(s)
        mark = [False] * len(target)
        mark2 = [False] * len(s)
        for i,v in enumerate(s):
            if i < len(target) and target[i] == v:
                mark[i] = True
                mark2[i] = True
                res.setCorrect(i)
                self.alphabet.setCorrect(self.alphabet.getWord().index(v))
        for i,v in enumerate(s):
            if mark2[i]:
                continue
            for i2, v2 in enumerate(target):
                if mark[i2]:
                    continue
                if v == v2:
                    mark[i2] = True
                    mark2[i] = True
                    res.setMisplaced(i)
                    if not self.alphabet.isCorrect(self.alphabet.getWord().index(v)):
                        self.alphabet.setMisplaced(self.alphabet.getWord().index(v))
        for i,v in enumerate(s):
            if not mark2[i]:
                res.setNotUsed(i)
                if self.alphabet.colorAt(self.alphabet.getWord().index(v)):
                    self.alphabet.setColorAt(self.alphabet.getWord().index(v), "red")
        self.guesses.append(res)
        return (target == s, res)
    def getWordleWord(self):
        return self.target
    def getGuessCount(self):
        return len(self.guesses)
    def getAlphabet(self):
        return self.alphabet
    def getGuess(self, i):
        assert i < len(self.guesses)
        return self.guesses[i]
    
