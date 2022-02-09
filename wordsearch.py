from wordbank import WordBank

class WSWord: # a word inside of the word search
    def __init__(self, x, y, dir, len, word):
        self.x = x
        self.y = y
        self.dir = dir
        self.word = word
class WordSearch:
    #initializes an empty matrix
    def __init__(self, w,h):
        self.guesses = []
        self.ch = [None] * h
        self.target = ""
        for i in self.ch:
            i = [None] * w
        self.commonwords = WordBank("commonwords.txt")
        self.allwords = WordBank("words_alpha.txt")
        self.allchars = WordBank("alphabet.txt")
    #tries to place a word in the generating wordsearch
    def placeWord(self, WSWord):
        (x, y) = (WSWord.x, WSWord.y)

    #generates the word search, returns target word
    def genWordSearch(self):
        tries = 0
        while tries < 5:
            maxmatch = 0
            maxmatchlist = []
        for i in self.ch:
            for x in self.ch:
                if x == None:
                    x = self.allchars.getRandom()

    def __str__(self):
        res = ""
        for i in self.ch:
            for x in self.ch:
                res += x
            res += '\n'
        return res