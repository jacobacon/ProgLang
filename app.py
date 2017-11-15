from parser import Parser

p = Parser()

sourcefile = open("language.run")

print p.languagelexer(sourcefile.read())

sourcefile.close()
