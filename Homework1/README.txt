uni: jpf2141
name: Josh Fram





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
The perplexity is 12.7128642612

A4:


A5:

python perplexity.py output/Sample1_scored.txt data/Brown_train.txt 
The perplexity is 1.55063515272

python perplexity.py output/Sample2_scored.txt data/Brown_train.txt 
The perplexity is 7.3135546517

Because our model was trained with the Brown dataset, it would make sense that data similar to that dataset would have a low perplexity. Therefore, it is likely that Sample1 is an excerpt of the Brown dataset, because the perplexity is very low (especially relative to the perplexity of Sample2).





