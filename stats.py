from sys import argv
from os import listdir,path
import operator
print 'Folderis: ', argv[1]
folder = argv[1]
total = ''
words = dict()
letters = dict()
for file in listdir(folder):
    if path.isfile(file):
        f = open(file, 'r')
        text = f.read()
        for word in text.split(' '):
            if word not in words.keys():
                words[word] = 0
            words[word] = words[word] + 1
        for letter in text:
            if letter not in letters.keys():
                letters[letter] = 0
            letters[letter] = letters[letter] + 1
        total += text
sorted_words = sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)
sorted_letters = sorted(letters.iteritems(), key=operator.itemgetter(1), reverse=True)
print sorted_words
print sorted_letters



