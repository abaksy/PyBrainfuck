# PyBrainfuck
A pure Python interpreter and REPL for the esoteric programming language called Brainfuck

The language manipulates a tape (considered to be of length 1024 in this implementation) of integers by using a single pointer 
to one cell in this tape

The symbols < and > are used to move left and right along the tape <br>
The symbols + and - respectively increment and decrement the content of the cell being currently pointed to <br>
The . symbol prints the ASCII value of the cell currently pointed to <br>
The , symbol asks for user input and stores that value to the cell currently pointed to <br>
The [] symbols are loop controls, all statements between [] are run in a loop until the value of the cell currently pointed to reaches 0

# Setup

Clone the repository to your local Linux machine, ```cd``` into the folder, and copy the output of the ```pwd``` command <br>
This will give the path to the PyBrainfuck folder

Now open the .bashrc folder using the command 

```
sudo nano ~/.bashrc
```
Add the following two lines to the very end of the .bashrc file

```
export PATH=$PATH:path-to-PyBrainfuck-folder
export PYBRAINFUCK=path-to-PyBrainfuck-folder
```

where path-to-PyBrainfuck-folder is the path you copied earlier. 

Now you can run the interpreter from any location on your system

# Usage

Run the following
```
bfc <script-file-path>
```
to run your own brainfuck scripts, or 
```
bfc
```
to run the Command Line Interface
