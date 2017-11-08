import sys


class Parser:

    def __init__(self):
        self.nextWord = " "
        self.wordlocation = 0
        return

    def languagelexer(self, inputfile):
        """Reads the file"""
        words = inputfile.split()  # Split the source code into an array of words

        # Somewhere along the line, create valid word list for valid input:

        # for word in words:
        #    if word not in validWordList:
        #        print(word, "is not a valid input")





        print(self.wordlocation)
        return self.nextWord
