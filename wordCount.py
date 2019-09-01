#! /usr/bin/env python3
import sys
import re
import os

# sys.argv: The list of command line arguments passed to a Python script.
# makes sure 3 arguments are passed
if len(sys.argv) is not 3:
    print('Correct usage: wordCount.py <input text file> <output file>')
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Check whether the text file exists ot not
#if not os.path.exists(inputFile):
#    print('text file input %s doesn\'t exist' % inputFile)
#    exit()

# Open the input and output files and read
input = open(inputFile , 'r+')
output = open(outputFile , 'w+')

# create the word dictionary, read and count all words, ignore white space and punctuations, and make all lower case
wordCount = {}
with open(inputFile , 'r') as inputFile:
    for text in inputFile:
        # removing white space
        # The strip() returns a copy of the string with both leading and trailing characters stripped.
        text = text.strip()
        # making uppercase letters lowercase
        text = text.casefold()
        # removing punctuations
        words = re.findall(r'[a-z]+' , text)
        for word in words:
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
input.close()

sortWordKey = sorted(wordCount.items())

with open(outputFile , 'w') as outputFile:
    for i in sortWordKey:
        outputFile.write("%s %d\n" % i)

output.close()
