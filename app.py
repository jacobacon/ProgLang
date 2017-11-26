from lexer import Lexer
import parser
import sys
import os.path

lexer = Lexer()

# This is the main entry point for code execution of Cookpy code.
# This file takes a single argument, which should point to the Cookpy code you want to run.
# If no argument is given, or if the file doesn't exist an error is raised.

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        sourcefile = open(sys.argv[1])
    else:
        raise StandardError("Usage Error: The SourceFile Doesn't Exist.")
else:
    raise StandardError('Usage Error: You Must Provide a Valid Source File to Run.')

# The lexer will read the file and return a list of valid words. Comments will be ignored.

tokens = lexer.languagelexer(sourcefile.read())
sourcefile.close()

# The parser will handle the rest of code execution.

parser.parser(tokens)

# If no error was raised in the parser, we exit with a 'clean' exit code.

sys.exit(0)
