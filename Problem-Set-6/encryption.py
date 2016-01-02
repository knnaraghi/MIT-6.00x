# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt" #change to proper directory

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("C:\Users\Khashayar\Downloads\MIT 6.00x\Week 6\code_ProblemSet6\story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    shifted_dictionary = {}
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    for letter in lower:
        # this is how you add a dictionary key-value pair in python
        # the left side is the key and the right side is the value
        shifted_dictionary[letter] = lower[(lower.index(letter) + shift) % 26]
    for letter in upper:
        shifted_dictionary[letter] = upper[(upper.index(letter) + shift) % 26]
    return shifted_dictionary

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encoded_text = ""
    for char in text:
        if char not in string.ascii_lowercase and char not in string.ascii_uppercase:
            encoded_text += char
        else:
            encoded_text += coder[char]
    return encoded_text

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.
    ### applies a shift given a text by calling applyCoder function described above
    ### which itself takes the text input and takes as second input the buildCoder module
    ### buildCoder is the function which incorporates the shift input
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    # set max number of words found in shifted text - initialized to zero first
    max_words_found = 0
    # best shift found - set to zero first
    best_shift = 0
    # for loop to apply shift for each iteration
    ##for p in string.punctuation:
        ##text = text.replace(p, '')
    for shift in range(0, 26):
        # shift the text
        shifted_text = applyShift(text, shift).split(' ')
        # split the text by spaces - seperating words
        ##shifted_text = shifted_text.
        valid_words = 0
        for word in shifted_text:
            if isWord(wordList, word) == True:
                valid_words += 1
            if valid_words > max_words_found:
                max_words_found = valid_words
                best_shift = shift
    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    #load the words
    words = loadWords()
    #load the decrypted story
    decrypted_story = getStoryString()
    #find the best shift
    shift = findBestShift(words, decrypted_story)
    # decryption of the story
    return applyShift(decrypted_story, shift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    ##wordList = loadWords()
    ##s = applyShift('Hello, world!', 8)
    ##bestShift = findBestShift(wordList, s)
    ##assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    decryptStory()
