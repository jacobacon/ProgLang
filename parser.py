import sys


class Parser:

    def __init__(self):

        SKIP = 'SKIP'
        VALID = 'VALID'
        COMMENT = 'COMMENT'


        self.pattern = [
            (r'[\n\t]+', SKIP),
            (r'#[^\n]*', COMMENT)




        ]





        return

    def languagelexer(self, inputfile):
        """Reads the file"""
        words = inputfile.split()  # Split the source code into an array of words

        validwords = []
        position = 0

        while position < len(words): # scan for valid regex
            match = None
            for token in self.pattern:
                pattern, tag = token

                position += 1



        print tag


        # Somewhere along the line, create valid word list for valid input:

        # for word in words:
        #    if word not in validWordList:
        #        print(word, "is not a valid input")
        return words
