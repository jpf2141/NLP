uni: jpf2141
name: Josh Fram




____________________________________
A1:

UNIGRAM near -12.4560686964
BIGRAM near the -1.56187888761 
TRIGRAM near the ecliptic -5.39231742278


A2: 
python perplexity.py output/A2.uni.txt data/Brown_train.txt 
The perplexity is 1052.4865859

python perplexity.py output/A2.bi.txt data/Brown_train.txt 
The perplexity is 53.8984761198

python perplexity.py output/A2.tri.txt data/Brown_train.txt 
The perplexity is 5.7106793082


A3:
python perplexity.py output/A3.txt data/Brown_train.txt 
The perplexity is 12.5516094886

A4:
These results were not that surprising, because we evenly weighted the trigram, bigram, and unigram probabilities in the linear interpolation function. Had we used weighted probabilities, I would have expected linearscore() to perform better than scores(), but due to the even weightings the relatively poor performance of linearscore() isn’t surprising.

A5:

python perplexity.py output/Sample1_scored.txt data/Sample1.txt 
The perplexity is 11.1670289158

python perplexity.py output/Sample2_scored.txt data/Sample2.txt 
The perplexity is 1611240282.44


Because our model was trained with the Brown dataset, it would make sense that data similar to that dataset would have a low perplexity. Therefore, it is likely that Sample1 is an excerpt of the Brown dataset, because the perplexity is very low (especially relative to the perplexity of Sample2).

____________________________________
B2:

TRIGRAM CONJ ADV NOUN -4.46650366731TRIGRAM DET NUM NOUN -0.713200128516TRIGRAM NOUN PRT CONJ -6.38503274104


B4:

* * 0.0midnight NOUN -13.1814628813Place VERB -15.4538814891
primary ADJ -10.0668014957
STOP STOP 0.0
_RARE_ VERB -3.17732085089
_RARE_ X -0.546359661497

B5:

python pos.py output/B5.txt data/Brown_tagged_dev.txt 
Percent correct tags: 93.1967869916

B6: 

python pos.py output/B6.txt data/Brown_tagged_dev.txt 
Percent correct tags: 91.3944534563


____________________________________
Execution Times:
Part A: 

python solutionsA.py 
Part A time: 16.39 sec


Part B:

ython solutionsB.py 
Part B time: 358.34 sec












