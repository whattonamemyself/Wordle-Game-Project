# Used to avoid circular imports

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