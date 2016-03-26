Josh Fram
jpf2141

1) Dependency Graphs

a. See images in HW2 root directory
/home/jpf2141/hidden/4468341106/Homework2/figure_da.png
/home/jpf2141/hidden/4468341106/Homework2/figure_en.png
/home/jpf2141/hidden/4468341106/Homework2/figure_ko.png
/home/jpf2141/hidden/4468341106/Homework2/figure_sw.png

b. In the dependency graph of a projective sentence, there are no edges that cross over one another. Therefore, by checking to see that there are not any word-to-word edges that cross with another word-to-word edge, we can make sure that the sentence is projective.

c.
Projective: I watch television.
Non-Projective: I drove a bus this week which was white.


2)

b.
Using the badfeatures model and the Swedish training corpus, the output was:

jpf2141@delhi:~/hidden/4468341106/Homework2$ python test.py 
 Number of training examples : 500
 Number of valid (projective) examples : 437
Training support vector machine...
done!
UAS: 0.279305354559 
LAS: 0.178726483357

Using the badfeatures model and the English training corpus, the output was:

jpf2141@delhi:~/hidden/4468341106/Homework2$ python test.py 
 Number of training examples : 200
 Number of valid (projective) examples : 200
Training support vector machine...
done!
UAS: 0.0567237163814 
LAS: 0.0

Relative to the other models, the badfeatures model has poor performance, particularly in languages other than Swedish (my guess is that it was trained on Swedish sentences…). The badfeatures model was trained without extensive feature extractions implemented, which is why the scores are so low when it is used. Information like the POS tags are not determined by the badfeatures model – when these are implemented in my featurextractor.py file, performance improves significantly. 

3)

a.
/home/jpf2141/hidden/4468341106/Homework2/featureextractor.py

Features:
'lemma': '_',
'ctag': tag,
'tag': tag,

Lemma:
Overview: The lemma of a word is the word as it appears in a dictionary (i.e. “words” appears as “word”). Using the lemma of a word allows us to better recognize different forms of the same word (for example, we can recognize the similarity between “words” and “word” after we take their lemma form).
Implementation: 
	If stack:
	1)Pop stack once and take the index of that item, then get that item’s token from the list of 	nodes in the dependency graph (i.e. from ‘tokens’). 
	2)Check to make sure ‘lemma’ is in the token and check to make sure the lemma is informative. 	3)Then, generate feature vector ‘STK_0_LEMMA_’.
	If buffer:
	1)Take the first item of the buffer the index of that item, then get that item’s token from 	the list of nodes in the dependency graph (i.e. from ‘tokens’). 
	2)Check to make sure ‘lemma’ is in the token and check to make sure the lemma is informative. 	3)Then, generate feature vector ‘BUF_0_LEMMA_’.
Performance: Implementing the lemma feature does not achieve a significant boost to performance. I experienced only around a 1% increase in scores. I think this is because lemma’s were not informative for many tokens.
Complexity: This feature is of order O(N), because it simply iterates through all the words in each sentence. Accessing the dictionary to find the lemmas is O(1), so it does not increase the complexity.

POS Tags (‘tag’ *and* ‘ctag’ features):
Overview: The POS of a word is the word’s part of speech (noun, verb, etc.). POS tags are very helpful in training model.
Implementation: 
	If stack:
	1)Pop stack once and take the index of that item, then get that item’s token from the list of 	nodes in the dependency graph (i.e. from ‘tokens’). 
	2a)Check to make sure ‘tag’ is in the token and check to make sure the ‘tag’ is informative.
	2b) Then, generate feature vector 'STK_0_POSTAG_'
	3a)Check to make sure ‘ctag’ is in the token and check to make sure the ‘tag’ is informative.
	3b) Then, generate feature vector 'STK_0_CPOSTAG_' 
	4) If the stack is greater than size 1, pop the stack again and repeat step 1, step 2a, 		4b)Generate feature vector ’STK_1_POSTAG_’.
	If buffer:
	1)Take first element of the buffer and take the index of that item, then get that item’s 		token from the list of nodes in the dependency graph (i.e. from ‘tokens’). 
	2a)Check to make sure ‘tag’ is in the token and check to make sure the ‘tag’ is informative.
	2b) Then, generate feature vector ‘BUF_0_POSTAG_'
	3a)Check to make sure ‘ctag’ is in the token and check to make sure the ‘tag’ is informative.
	3b) Then, generate feature vector ‘BUF_0_CPOSTAG_' 
	4) If the buffer is greater than size 1, take 2nd element of the buffer and repeat step 1, 	step 2a.		
	4b)Generate feature vector ’BUF_1_POSTAG_’.
	5) If the stack is greater than size 2, take 3rd element of the buffer and repeat step 1, 		step 2a
	5b)Generate feature vector ’BUF_2_POSTAG_’.
Performance: POS tagging is probably the most important feature that could have been implemented. By adding both these features (coarse-grained POS and regular POS tagging), I gain approximately 45% performance. CPOSTAGing serves as more of a supplement to regular POS tagging, adding by itself about 1-2% to performance. Evidently, POS tagging is an important feature. 
Complexity: This feature is of order O(N), because it simply iterates through all the words in each sentence. Accessing the dictionary to label is O(1), so it does not increase the complexity.


b.
/home/jpf2141/hidden/4468341106/Homework2/swedish.model
/home/jpf2141/hidden/4468341106/Homework2/english.model
/home/jpf2141/hidden/4468341106/Homework2/danish.model



c.
Swedish:
jpf2141@delhi:~/hidden/4468341106/Homework2$ python test.py 
This is not a very good feature extractor!
 Number of training examples : 500
 Number of valid (projective) examples : 437
Training support vector machine...
done!
UAS: 0.818379160637 
LAS: 0.725759768452

English:
pf2141@delhi:~/hidden/4468341106/Homework2$ python test.py 
 Number of training examples : 200
 Number of valid (projective) examples : 200
Training support vector machine...
done!
UAS: 0.796577017115 
LAS: 0.763325183374

Danish:
jpf2141@delhi:~/hidden/4468341106/Homework2$ python test.py 
 Number of training examples : 200
 Number of valid (projective) examples : 165
Training support vector machine...
done!
UAS: 0.803895231699 
LAS: 0.711887172599

d.
The arc-eager parser has O(N) time complexity (N being the number of words in the sentence). It is a bottom-up parser, and the time complexity is much better than related top-down parsers.
A big disadvantage of the arc-eager parser is that it cannot parse non-projective sentences, which is quite limiting in that it makes it so the parser can’t parse all sentences in a language. Another disadvantage is that you have to train a model to allow the arc-eager parser to correctly decide which transition to make. 
