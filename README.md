# PyBrainfuck
A pure Python interpreter and REPL for the esoteric programming language called Brainfuck

The language manipulates a tape (considered to be of length 1024 in this implementation) of integers by using a single pointer 
to one cell in this tape

The symbols < and > are used to move left and right along the tape
The symbols + and - respectively increment and decrement the content of the cell being currently pointed to
The . symbol prints the ASCII value of the cell currently pointed to
The , symbol asks for user input and stores that value to the cell currently pointed to
The [] symbols are loop controls
All statements between [] are run in a loop until the value of the cell currently pointed to reaches 0

## Usage

To run the Brainfuck interpreter on your system (Linux), clone the repository and then add the current working directory to
the PATH variable using the terminal command 
```
$ export PATH=$PATH:path-to-PyBrainfuck
```
where path-to-PyBrainfuck is the location of the folder, for example ~/PyBrainfuck

This will only temporarily affect the system. If you want the changes to persist then use the following

```
$ sudo nano ~/.bashrc
```
After the .bashrc file opens in nano, add the export command above at the end of the file

Once the folder is added to PATH, you can use the interpreter to interpret your own Brainfuck scripts

```
$ bfc <filename.txt>
```

The REPL (Read-Eval-Print Loop) can be used by simply typing 

```
$ bfc
```
into the terminal
