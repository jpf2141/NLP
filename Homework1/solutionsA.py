import math
import nltk
import time
from collections import Counter

# Constants to be used by you when you fill the functions
START_SYMBOL = '*'
STOP_SYMBOL = 'STOP'
MINUS_INFINITY_SENTENCE_LOG_PROB = -1000

# TODO: IMPLEMENT THIS FUNCTION
# Calculates unigram, bigram, and trigram probabilities given a training corpus
# training_corpus: is a list of the sentences. Each sentence is a string with tokens separated by spaces, ending in a newline character.
# This function outputs three python dictionaries, where the keys are tuples expressing the ngram and the value is the log probability of that ngram
def calc_probabilities(training_corpus):
    unigram_p = {}
    bigram_p = {}
    trigram_p = {}
    unigram_tuples = []
    bigram_tuples = []
    trigram_tuples = []
    word_total = 0
    bigram_total = 0
    trigram_total = 0
    
    for line in training_corpus:
        line = START_SYMBOL + " " + START_SYMBOL + " " + line + " " + STOP_SYMBOL
        tokens = line.split()
        line_bigrams = list(nltk.bigrams(tokens))
        line_trigrams = list(nltk.trigrams(tokens))
        
        unigram_tuples.extend(tokens)
        bigram_tuples.extend(line_bigrams)
        trigram_tuples.extend(line_trigrams)
    
        word_total = word_total + (len(tokens) - 2)
        bigram_total = bigram_total + (len(line_bigrams) - 1)
        trigram_total = trigram_total + (len(line_trigrams))

    unigram_counts = Counter(unigram_tuples)
    unigram_counts[START_SYMBOL] /= 2
    bigram_counts = Counter(bigram_tuples)
    trigram_counts = Counter(trigram_tuples)

    for unigram, unigram_count in unigram_counts.items():
        probability = (1.0 * unigram_count)/ word_total
        
        log_probability = math.log(probability, 2)
        unigram = tuple([unigram])
        unigram_p[unigram] = log_probability

    for bigram, bigram_count in bigram_counts.items():
        unigram_count = unigram_counts[bigram[0]]   #count of first word in bigram
        
        probability = (1.0 * bigram_count)/unigram_count   #conditional probability
        log_probability = math.log(probability, 2)
        bigram_p[bigram] = log_probability

    for trigram, trigram_count in trigram_counts.items():
        bigram_count = bigram_counts[(trigram[0], trigram[1])]

        probability = (1.0 * trigram_count)/bigram_count
        log_probability = math.log(probability, 2)
        trigram_p[trigram] = log_probability

    return unigram_p, bigram_p, trigram_p

# Prints the output for q1
# Each input is a python dictionary where keys are a tuple expressing the ngram, and the value is the log probability of that ngram
def q1_output(unigrams, bigrams, trigrams, filename):
    # output probabilities
    outfile = open(filename, 'w')

    unigrams_keys = unigrams.keys()
    unigrams_keys.sort()
    for unigram in unigrams_keys:
        outfile.write('UNIGRAM ' + unigram[0] + ' ' + str(unigrams[unigram]) + '\n')

    bigrams_keys = bigrams.keys()
    bigrams_keys.sort()
    for bigram in bigrams_keys:
        outfile.write('BIGRAM ' + bigram[0] + ' ' + bigram[1]  + ' ' + str(bigrams[bigram]) + '\n')

    trigrams_keys = trigrams.keys()
    trigrams_keys.sort()    
    for trigram in trigrams_keys:
        outfile.write('TRIGRAM ' + trigram[0] + ' ' + trigram[1] + ' ' + trigram[2] + ' ' + str(trigrams[trigram]) + '\n')
    outfile.close()


# TODO: IMPLEMENT THIS FUNCTION
# Calculates scores (log probabilities) for every sentence
# ngram_p: python dictionary of probabilities of uni-, bi- and trigrams.
# n: size of the ngram you want to use to compute probabilities
# corpus: list of sentences to score. Each sentence is a string with tokens separated by spaces, ending in a newline character.
# This function must return a python list of scores, where the first element is the score of the first sentence, etc. 
def score(ngram_p, n, corpus):
    scores = []
    for line in corpus:
        product = 0;
        if n == 1:
            line = line + " " + STOP_SYMBOL
            tokens = line.split()
            for token in tokens:
                myTuple = tuple([token])
                if(myTuple in ngram_p):
                    probability = ngram_p[myTuple]
                    product += probability
                else:
                    product = MINUS_INFINITY_SENTENCE_LOG_PROB
                    break
            scores.append(product)
        elif n == 2:
            line = START_SYMBOL + " " + line + " " + STOP_SYMBOL
            tokens = line.split()
            line_bigrams = list(nltk.bigrams(tokens))
            for bigram in line_bigrams:
                if(bigram in ngram_p):
                    probability = ngram_p[bigram]
                    product += probability
                else:
                    product = MINUS_INFINITY_SENTENCE_LOG_PROB
                    break
            scores.append(product)
        elif n == 3:
            line = START_SYMBOL + " " + START_SYMBOL + " " + line + " " + STOP_SYMBOL
            tokens = line.split()
            line_trigrams = list(nltk.trigrams(tokens))
            for trigram in line_trigrams:
                if(trigram in ngram_p):
                    probability = ngram_p[trigram]
                    product += probability
                else:
                    product = MINUS_INFINITY_SENTENCE_LOG_PROB
                    break
            scores.append(product)
    return scores

# Outputs a score to a file
# scores: list of scores
# filename: is the output file name
def score_output(scores, filename):
    outfile = open(filename, 'w')
    for score in scores:
        outfile.write(str(score) + '\n')
    outfile.close()

# TODO: IMPLEMENT THIS FUNCTION
# Calculates scores (log probabilities) for every sentence with a linearly interpolated model
# Each ngram argument is a python dictionary where the keys are tuples that express an ngram and the value is the log probability of that ngram
# Like score(), this function returns a python list of scores
def linearscore(unigrams, bigrams, trigrams, corpus):
    scores = []
    

    for line in corpus:
        score = 0
        LMDA = 1.0/3
        tokenIndex = 2
        line = START_SYMBOL + " " + START_SYMBOL + " " + line + " " + STOP_SYMBOL
        tokens = line.split()
        for token in tokens[2:]:
            trigram = tuple([tokens[tokenIndex-2], tokens[tokenIndex-1], token])
            bigram = tuple([trigram[1], trigram[2]])
            unigram = tuple([bigram[1]])
            
            tokenIndex = tokenIndex + 1
            if (unigram not in  unigrams and bigram not in bigrams and trigram not in trigrams):
                score = MINUS_INFINITY_SENTENCE_LOG_PROB
                break
            else:
                triProb = math.pow(2, trigrams.get(trigram, MINUS_INFINITY_SENTENCE_LOG_PROB))
                biProb = math.pow(2, bigrams.get(bigram, MINUS_INFINITY_SENTENCE_LOG_PROB))
                uniProb = math.pow(2, unigrams.get(unigram, MINUS_INFINITY_SENTENCE_LOG_PROB))
            
                score += math.log(((triProb + biProb + uniProb) * LMDA), 2)
            
        scores.append(score)
    return scores

DATA_PATH = 'data/'
OUTPUT_PATH = 'output/'

# DO NOT MODIFY THE MAIN FUNCTION
def main():
    # start timer
    time.clock()

    # get data
    infile = open(DATA_PATH + 'Brown_train.txt', 'r')
    corpus = infile.readlines()
    infile.close()

    # calculate ngram probabilities (question 1)
    unigrams, bigrams, trigrams = calc_probabilities(corpus)

    # question 1 output
    q1_output(unigrams, bigrams, trigrams, OUTPUT_PATH + 'A1.txt')

    # score sentences (question 2)
    uniscores = score(unigrams, 1, corpus)
    biscores = score(bigrams, 2, corpus)
    triscores = score(trigrams, 3, corpus)

    # question 2 output
    score_output(uniscores, OUTPUT_PATH + 'A2.uni.txt')
    score_output(biscores, OUTPUT_PATH + 'A2.bi.txt')
    score_output(triscores, OUTPUT_PATH + 'A2.tri.txt')

    # linear interpolation (question 3)
    linearscores = linearscore(unigrams, bigrams, trigrams, corpus)

    # question 3 output
    score_output(linearscores, OUTPUT_PATH + 'A3.txt')

    # open Sample1 and Sample2 (question 5)
    infile = open(DATA_PATH + 'Sample1.txt', 'r')
    sample1 = infile.readlines()
    infile.close()
    infile = open(DATA_PATH + 'Sample2.txt', 'r')
    sample2 = infile.readlines()
    infile.close() 

    # score the samples
    sample1scores = linearscore(unigrams, bigrams, trigrams, sample1)
    sample2scores = linearscore(unigrams, bigrams, trigrams, sample2)

    # question 5 output
    score_output(sample1scores, OUTPUT_PATH + 'Sample1_scored.txt')
    score_output(sample2scores, OUTPUT_PATH + 'Sample2_scored.txt')

    # print total time to run Part A
    print "Part A time: " + str(time.clock()) + ' sec'

if __name__ == "__main__": main()
