Intro to Python:

To run the program do the following:

Clone the repository

Use the following command to run the program : 

        python wordCount.py declaration.txt output.txt
        
Use the following command to test the program : 

        python wordCountTest.py declaration.txt output.txt declarationKey.txt

Python version used: 3.7

For this project, the following people helped me in understanding it better:

Jazmin Paz (helped me with removing punctuations)

Samarah Jorgensen (helped me understand why the command uses three text files and not just two (reason is to test))

Jaime Salas (helped me understand why i needed the sys library)

The following are the project instruction:

This repository contains the code for the python introduction lab. The purpose is to have a fairly simple python assignment that introduces the basic features and tools of python

In the repository are two plain text files with lots of words. Your assignment is to create a python 2 program which:

takes as input the name of an input file and output file
example

$ python wordCount.py input.txt output.txt

keeps track of the total the number of times each word occurs in the text file
excluding white space and punctuation
is case-insensitive
print out to the output file (overwriting if it exists) the list of words sorted in descending order with their respective totals separated by a space, one word per line
To test your program we provide wordCountTest.py and two key files. This test program takes your output file and notes any differences with the key file. An example use is:

$ python wordCountTest.py declaration.txt myOutput.txt declarationKey.txt

The re regular expression library and python dictionaries should be used in your program.

Note that there are two major dialects of Python. Python 3.* is incompatible with 2*. As a result, Python 2.7 remains popular. All of our examples were ported to 3.* during the summer of 2018. We (mildly) encourage students to use that dialect of Python.
