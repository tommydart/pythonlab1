from sys import argv
from os import listdir,path
import operator

print 'Folderis:', argv[1]
folder = argv[1]

class FolderStats:
    words = dict()
    letters = dict()
    folder = ''

    def __init__(self, folderName):
        self.folder = folderName

    def read_stats(self):
        self.folder_stats(folder)

    def folder_stats(self, folder):
        if path.isdir(folder):
            for file in listdir(folder):
                self.folder_stats(folder + "\\" + file)
        else:
            file_words, file_letters = self.file_stats(folder)
            for word in file_words:
                if word not in self.words.keys():
                    self.words[word] = 0
                self.words[word] += file_words[word]
            for letter in file_letters:
                if letter not in self.letters.keys():
                    self.letters[letter] = 0
                self.letters[letter] += file_letters[letter]

    def file_stats(self, file):
        words = dict()
        letters = dict()
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
        return words, letters




stats = FolderStats(argv[1])
stats.read_stats()
sorted_words = sorted(stats.words.iteritems(), key=operator.itemgetter(1), reverse=True)
sorted_letters = sorted(stats.letters.iteritems(), key=operator.itemgetter(1), reverse=True)

print sorted_words
print sorted_letters
#for file in listdir(folder):
 #   if path.isfile(file):
  #      f = open(file, 'r')
   #     text = f.read()
    #    for word in text.split(' '):
     #       if word not in words.keys():
      #          words[word] = 0
       #     words[word] = words[word] + 1
       # for letter in text:
       #     if letter not in letters.keys():
       #         letters[letter] = 0
       #     letters[letter] = letters[letter] + 1
       # total += text
#sorted_words = sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)
#sorted_letters = sorted(letters.iteritems(), key=operator.itemgetter(1), reverse=True)
#print sorted_words
#print sorted_letters



