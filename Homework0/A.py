import nltk
import sys


squirrel = 0
girl = 0
greeting = sys.stdin.read()

print greeting

token_list = nltk.word_tokenize(greeting)
print "The tokens in the greeting are"

for token in token_list:
    lowerToken = token.lower()
    if lowerToken == "squirrel":
        squirrel += 1
    elif lowerToken == "girl":
        girl += 1
    print token

print "There were %d instances of the word 'squirrel' and %d instances of the word 'girl.'" % (squirrel, girl)
