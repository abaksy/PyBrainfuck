import sys
import interpreter
import process

tape = [0]*1024
index = 0  #Pointer to cell on tape

f = open(sys.argv[1])
text = f.read()
text = process.clean(text)
if interpreter.run(text, index, tape)==-1:
    print("Compilation Unsuccessful!")