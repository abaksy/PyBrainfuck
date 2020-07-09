import interpreter
code = ""
tape = [0]*1024
cell_index = 1
index = 0
while code != "!":
    code = input(f"\n[{cell_index}]: ")
    index = interpreter.run(code, index, tape)
    if index == -1:
        print("Error occured!")
    cell_index+=1