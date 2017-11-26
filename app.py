from lexer import Lexer
import parser
import sys
import os.path

lexer = Lexer()

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        sourcefile = open(sys.argv[1])
    else:
        raise StandardError("Usage Error: The SourceFile Doesn't Exist.")
else:
    raise StandardError('Usage Error: You Must Provide a Valid Source File to Run.')

tokens = lexer.languagelexer(sourcefile.read())
sourcefile.close()

parser.parser(tokens)

sys.exit(0)
