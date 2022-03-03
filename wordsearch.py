from wordbank import WordBank
import random

commonwords = WordBank("commonwords.txt")
allwords = WordBank("words_alpha.txt")
allchars = WordBank("alphabet.txt")
#delta towards a direction
direction = [
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,-1)
]
class WSWord: # a word inside of the word search
    def __init__(self, x, y, dir, word):
        self.x = x
        self.y = y
        self.dir = dir
        self.word = word
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getLen(self):
        return len(self.word)
    def getDir(self):
        return self.dir
    def getWord(self):
        return self.word
class WordSearch:
    #initializes an empty matrix
    def __init__(self, w,h):
        assert w > 0
        assert h > 0
        self.guesses = []
        self.ch = [None] * w
        self.target = ""
        self.wordlist = []
        for i in range(len(self.ch)):
            self.ch[i] = [None] * h
    #can you place the word in the wordsearch? returns # of characters already placed, -1 if can't place
    def canPlace(self, wsword):
        (x, y) = (wsword.getX(), wsword.getY())
        dir = wsword.getDir()
        res = 0
        word = wsword.getWord()
        for ch in word:
            if x < 0 or y < 0 or x >= len(self.ch) or y >= len(self.ch[0]): #out of bounds
                return -1 
            if self.ch[x][y] == ch:
                res += 1
            elif not self.ch[x][y] == None:
                return -1
            #is there a shortcut to this?
            x += direction[dir][0]
            y += direction[dir][1]
        return res

    def placeWord(self, wsword): #places word //note: assumes that the word can be placed
        (x, y) = (wsword.getX(), wsword.getY())
        dir = wsword.getDir()
        word = wsword.getWord()
        for ch in word:
            self.ch[x][y] = ch
            x += direction[dir][0]
            y += direction[dir][1]
    
    #generates a partial wordsearch, i broke it into parts to increase efficiency as 16*10^4 is faster than 40^4
    def genPartialWordSearch(self, xPos, yPos, width, height):
        tries = 0
        while tries < 5:
            s = []
            for i in range(8):
                word = ""
                while True:
                    word = commonwords.getRandom()
                    if word in self.wordlist:
                        continue
                    if len(word) <= 6: #encourages shorter words
                        break
                    elif len(word) <= 8 and random.randint(0,1) == 0: #1/2 chance
                        break
                    elif len(word) > 8 and random.randint(0,5) == 0: # 1/6 chance
                        break

                s.append(commonwords.getRandom())
            maxmatch = 0
            maxmatchlist = []
            #some dumb brute force algo trying to place the word in every slot possible
            for i in range(width):
                for x in range(height):
                    for dir in range(8):
                        for word in s:
                            wsword = WSWord(i + xPos,x + yPos,dir,word)
                            tmp = self.canPlace(wsword)
                            if tmp > maxmatch: #maximise overlapping
                                maxmatch = tmp
                                maxmatchlist = [wsword]
                            elif tmp == maxmatch:
                                maxmatchlist.append(wsword)
            #i want to maximise overlapping, so i reduced the chances if it doesnt overlap
            if maxmatch == 0 and random.randint(0,2) != 0: 
                continue
            if len(maxmatchlist):
                tries = 0
                chosen = random.choice(maxmatchlist)
                self.placeWord(chosen)
                self.wordlist.append(chosen.getWord())
            else:
                tries += 1
        
    #generates the word search, returns target word
    def genWordSearch(self):
        width = 5
        height = 5
        positions = []
        for x in range(len(self.ch[0])//height):
            for i in range(len(self.ch)//width):
                xPos = i*width
                yPos = x*height
                width2 = min(width, len(self.ch) - xPos)
                height2 = min(height, len(self.ch[0])-yPos)
                positions.append([xPos, yPos, width2, height2])
        random.shuffle(positions)
        for i in positions:
            self.genPartialWordSearch(i[0], i[1], i[2], i[3])
        #fill in the rest
        for i in range(len(self.ch)):
            for x in range(len(self.ch[0])):
                if self.ch[i][x] == None:
                    self.ch[i][x] = allchars.getRandom()
        print(len(self.wordlist))
        self.target = random.choice(self.wordlist)
        return self.target
    #returns the string of text
    def getWord(self, x, y, dir, len2):
        res = ""
        for i in range(len2):
            if x < 0 or y < 0 or x >= len(self.ch) or y >= len(self.ch[0]): #out of bounds
                continue
            res += self.ch[x][y]
            x += direction[dir][0]
            y += direction[dir][1]
        return res
    #highlights the word you're guessing, and returns it / returns -1 if it is not a word
    def guess(self, x, y, dir, len):
        word = self.getWord(x,y,dir,len)
        if allwords.contains(word):
            self.guesses.append(WSWord(x,y,dir,word))
            return word
        else:
            return -1
    #returns a list of all the highlighted words on the wordsearch
    def getGuesses(self):
        return self.guesses
    #returns the target word
    def getTarget(self):
        return self.target
    def __str__(self):
        res = ""
        for i in range(len(self.ch[0])):
            for x in range(len(self.ch)):
                if self.ch[x][i] == None:
                    res += "_ "
                else:
                    res += self.ch[x][i] + " "
            res += '\n'
        return res
    def getWidth(self):
        return len(self.ch)
    def getHeight(self):
        return len(self.ch[0])
    def getGrid(self):
        return self.ch

def main():
    x = WordSearch(24,14)
    target = x.genWordSearch()
    print(target)
    print(x)

if __name__ == "__main__":
    main()