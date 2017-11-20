from lexer import Lexer
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


print lexer.languagelexer(sourcefile.read())

sourcefile.close()
