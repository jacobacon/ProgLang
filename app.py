from lexer import Lexer
from stack import Stack
import sys
import os.path

lexer = Lexer()
stack = Stack()

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        sourcefile = open(sys.argv[1])
    else:
        print("Usage Error: The SourceFile Doesn't Exist.")
else:
    print('Usage Error: You Must Provide a Valid Source File to Run.')
    sys.exit(1)


words = lexer.languagelexer(sourcefile.read())
sourcefile.close()

print words

for word in words:
    stack.push(word)

print stack.isempty()
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()


