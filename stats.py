 #!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from os import listdir,path
import operator

print 'Folderis:', argv[1]
folder = argv[1]
file_out = argv[2]
class FolderStats:
    words = dict()
    letters = dict()
    folder = ''
    files_stats = ''
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
            sorted_words = sorted(file_words.iteritems(), key=operator.itemgetter(1), reverse=True)
            sorted_letters = sorted(file_letters.iteritems(), key=operator.itemgetter(1), reverse=True)

            self.files_stats += "\nFailas: "
            self.files_stats += folder
            self.files_stats += "\nPasikartojantys žodžiai (pagal dažnumą):\n"
            self.files_stats += str(sorted_words)
            self.files_stats += "\nPasikartojantys simboliai (pagal dažnumą):\n"
            self.files_stats += str(sorted_letters)
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

f = open(file_out, 'w')
f.write("Pasikartojantys žodžiai (pagal dažnumą):\n")
f.write(str(sorted_words))
f.write("\nPasikartojantys simboliai (pagal dažnumą):\n")
f.write(str(sorted_letters))

f.write("\nAtskirų failų statistika:")
f.write(stats.files_stats)



