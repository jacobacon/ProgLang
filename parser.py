import sys


class Parser:

    def __init__(self):
        self.nextWord = " "
        self.wordlocation = 0
        return

    def languagelexer(self, inputfile):
        """Reads the file"""
        words = inputfile.split()  # Split the source code into an array of words

        def findnextword():
            if self.wordlocation > len(words):
                return ""
            else:
                returnvalue = words[self.wordlocation]
                self.wordlocation = self.wordlocation+1
                return returnvalue

        self.nextWord = findnextword()  # Find the next word, and return it.
        print(self.wordlocation)
        return self.nextWord
