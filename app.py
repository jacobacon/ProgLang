from lexer import Lexer
import parser
import sys
import os.path

lexer = Lexer()

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        sourcefile = open(sys.argv[1])
    else:
        print("Usage Error: The SourceFile Doesn't Exist.")
else:
    print('Usage Error: You Must Provide a Valid Source File to Run.')
    sys.exit(1)


tokens = lexer.languagelexer(sourcefile.read())
sourcefile.close()

parser.parser(tokens)

parser.add_to_stack(5)
parser.add_to_stack(1)

parser.check_dictionary('subtract')

print(parser.return_stack())
sys.exit(0)

