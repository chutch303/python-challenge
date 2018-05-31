import pandas as pd

with open(r"C:\Users\chutc\paragraph_1.txt") as f:
    data=f.read()

print("Paragraph Analysis")
print("-----------------------------")

for sent in data.split("."):
    print(sent)
    print()

# number of sentences. counting number of times it split on a period
print("Number of Sentences = " + str(len(data.split("."))))

# number of words in the doc. counting the # of times it split on space
print("Number of Words = " + str(len(data.split())))

#average sentence length = # of words / # of sentences
print("Average Sentence Length = " + str(len(data.split()) / len(data.split("."))))

import string
letters = string.ascii_letters

letter_count = 0

for s in data:
    if s in letters:
        letter_count +=1

letter_count

#Average letter count per word = total letter count / # of words
#how to get letter count????/
print("Average letter count per word = " + str(letter_count / len(data.split())))