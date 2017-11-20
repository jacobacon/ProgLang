import sys
import re


class Lexer:

    #Initial values in the class
    def __init__(self):

        # Tokens for handling words
        self.SKIP = 'SKIP'
        self.VALID = 'VALID'
        self.COMMENT = 'COMMENT'

        # Regex patterns for handling words
        self.patterns = [
            (re.compile(r'^[^A-Za-z0-9._%]+$'), self.SKIP),
            (re.compile(r'%%[^\n]*'), self.COMMENT),
            (re.compile(r'^[A-Za-z0-9._]+$'), self.VALID)
        ]
        return

    def languagelexer(self, inputfile):
        """Reads the file and returns valid words, and filters out invalid words and comments"""
        words = inputfile.split()  # Split the source code into an array of words

        # If the '%%' word is found, a comment follows until another '%%' is found.
        comment = False
        validtokens = []

        for word in words:

            for regex in self.patterns:
                pattern, tag = regex

                match = pattern.match(word)
                if match:
                    print tag + word
                    if (tag == self.SKIP) and (comment == False):
                        print 'Syntax Error: Invalid Token + ' + word
                        sys.exit(1)
                    if (tag == self.COMMENT) and (comment == False):
                        print 'Comment Found'
                        comment = True
                        continue
                    elif (tag == self.COMMENT) and (comment == True):
                        comment = False
                        continue
                    elif (tag == self.VALID) and (comment == False):
                        validtokens.append(word)
        return validtokens
