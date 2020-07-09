import process

def run(text, index, tape):
    i=0
    bracket_indices = process.bracket_matching(text)
    while i < len(text):
        if text[i] == '+':
            tape[index] += 1  #Increment value at current cell
        elif text[i] == '-':
            tape[index] -= 1    #Decrement value at current cell
        elif text[i] == '>':
            index += 1          #Move pointer to the right
        elif text[i] == '<':
            index -= 1          #Move pointer to the left
        elif text[i] == '.':
            print(chr(tape[index]), end='')  #Print value at current cell to stdout
        elif text[i] == ',':
            tape[index] = int(input("Enter something: "))  #Accept input and store in current cell
        elif text[i] == '[':
            try:                                           #Loop open
                #print(f"[ found at index {i}")
                try:
                    bracket_close_index = bracket_indices[i]
                except KeyError:
                    print(f"No closing brace found for opening bracket at index {i}")
                    return -1
                loopcode = text[i+1:bracket_close_index]
                while True:
                    if tape[index] == 0:
                        break
                    else:
                        #print("Looping through ", loopcode, " pointer at ", index)
                        index = run(loopcode, index, tape)
                i = bracket_close_index
            except ValueError:
                print("Syntax Error! Opening [ was not matched")
        #print(tape[0:20])
        i+=1
    return index