import requests
from bs4 import BeautifulSoup
import operator

def listOfWords(url):
    word_list = []
    # Getting that html stuff that doesn't tell a human much
    sourceCode = requests.get(url)
    # Text, images, etc of a website
    plainText = sourceCode.text
    # BeautifulSoup needs data formatted in a special way to be able to sift through it easily
    soup = BeautifulSoup(plainText, features="html.parser")

    # Get all the body text
    for d in soup.findAll('div', {'class': 'infinite-item'}):
        text = d.findAll('p')
        for t in text:
            body = t.string
            if body is None:
                pass
            else:
                words = body.lower().split()
                for word in words:
                    word_list.append(word)

    cleanList(word_list)

# Get rid of any symbols in the words in the list
def cleanList(list):
    clean_word_list = []
    symbols = '~!@#$%^&*()_+|}{":?></.,;][=0987654321]'
    symbolsLength = len(symbols)
    for word in list:
        for i in range(0, symbolsLength):
            # Replace symbols in the word with empty string
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            if 'â' in word:
                pass
            else:
                clean_word_list.append(word)
    createDictionary(clean_word_list)

# Count the amount of times the word shows up on the site
def createDictionary(list):
    wordCount = {}
    for word in list:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    # operator.itemgetter(1) sorts by value, if it were 0 it would sort by key
    for key, value in sorted(wordCount.items(), key=operator.itemgetter(1)):
        print(key + ":", value)


listOfWords('https://animals.howstuffworks.com/arachnids/spider.htm')