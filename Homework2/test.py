
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition
from datetime import datetime
import random

if __name__ == '__main__':
    traindata = dataset.get_english_train_corpus().parsed_sents()

#    sample_size = 500
#    dt = datetime.now()
#    time_seed = dt.microsecond % 10000
#    print dt, time_seed
#    random.seed(time_seed)
#    training_sample = random.sample(traindata, sample_size)

    try:
        
        tp = TransitionParser(Transition, FeatureExtractor)
        tp.train(traindata)
        tp.save('english.model')
        
        labeleddata = dataset.get_english_dev_corpus().parsed_sents()
        blinddata = dataset.get_english_dev_blind_corpus().parsed_sents()
        #tp = TransitionParser.load('badfeatures.model')
        
        parsed = tp.parse(blinddata)
        
        with open('test.conll', 'w') as f:
            for p in parsed:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')
    
        ev = DependencyEvaluator(labeleddata, parsed)
        print "UAS: {} \nLAS: {}".format(*ev.eval())

# parsing arbitrary sentences (english):
# sentence = DependencyGraph.from_sentence('Hi, this is a test')

# tp = TransitionParser.load('english.model')
# parsed = tp.parse([sentence])
# print parsed[0].to_conll(10).encode('utf-8')
    except NotImplementedError:
        print """
        This file is currently broken! We removed the implementation of Transition
        (in transition.py), which tells the transitionparser how to go from one
        Configuration to another Configuration. This is an essential part of the
        arc-eager dependency parsing algorithm, so you should probably fix that :)
        
        The algorithm is described in great detail here:
        http://aclweb.org/anthology//C/C12/C12-1059.pdf
        
        We also haven't actually implemented most of the features for for the
        support vector machine (in featureextractor.py), so as you might expect the
        evaluator is going to give you somewhat bad results...
        
        Your output should look something like this:
        
        UAS: 0.23023302131
        LAS: 0.125273849831
        
        Not this:
        
        Traceback (most recent call last):
        File "test.py", line 41, in <module>
        ...
        NotImplementedError: Please implement shift!
        
        
        """
#from providedcode import dataset
#from providedcode.transitionparser import TransitionParser
#from providedcode.evaluate import DependencyEvaluator
#from featureextractor import FeatureExtractor
#from transition import Transition
#from datetime import datetime
#import random
#
#if __name__ == '__main__':
#    #traindata = dataset.get_swedish_train_corpus().parsed_sents()
#    #traindata = dataset.get_korean_train_corpus().parsed_sents()
#    #traindata = dataset.get_english_train_corpus().parsed_sents()
#    traindata = dataset.get_danish_train_corpus().parsed_sents()
#    
#    sample_size = 100
#    dt = datetime.now()
#    time_seed = dt.microsecond % 10000
#    print dt, time_seed
#    random.seed(time_seed)
#    training_sample = random.sample(traindata, sample_size)
#    
#    try:
#        tp = TransitionParser(Transition, FeatureExtractor)
#        tp.train(training_sample)
#        #tp.save('danish.model')
#        #tp.save('korean.model')
#        #tp.save('english.model')
#        tp.save('swedish.model')
#
#        #labeleddata = dataset.get_danish_dev_corpus().parsed_sents()
#        #labeleddata = dataset.get_korean_dev_corpus().parsed_sents()
#        #labeleddata = dataset.get_english_dev_corpus().parsed_sents()
#        labeleddata = dataset.get_swedish_dev_corpus().parsed_sents()
#        
#        blinddata = dataset.get_swedish_dev_blind_corpus().parsed_sents()
#        
#        #tp = TransitionParser.load('badfeatures.model')
#        #tp = TransitionParser.load('swedish.model')
#        #tp = TransitionParser.load('korean.model')
#        tp = TransitionParser.load('badfeatures.model')
#        
#        parsed = tp.parse(blinddata)
#        
#        with open('test.conll', 'w') as f:
#            for p in parsed:
#                f.write(p.to_conll(10).encode('utf-8'))
#                f.write('\n')
#    
#        ev = DependencyEvaluator(labeleddata, parsed)
#        print "UAS: {} \nLAS: {}".format(*ev.eval())
#
#        # parsing arbitrary sentences (english):
#        # sentence = DependencyGraph.from_sentence('Hi, this is a test')
#
#        # tp = TransitionParser.load('english.model')
#        # parsed = tp.parse([sentence])
#        # print parsed[0].to_conll(10).encode('utf-8')
#    except NotImplementedError:
#        print """
#        This file is currently broken! We removed the implementation of Transition
#        (in transition.py), which tells the transitionparser how to go from one
#        Configuration to another Configuration. This is an essential part of the
#        arc-eager dependency parsing algorithm, so you should probably fix that :)
#        
#        The algorithm is described in great detail here:
#        http://aclweb.org/anthology//C/C12/C12-1059.pdf
#        
#        We also haven't actually implemented most of the features for for the
#        support vector machine (in featureextractor.py), so as you might expect the
#        evaluator is going to give you somewhat bad results...
#        
#        Your output should look something like this:
#        
#        UAS: 0.23023302131
#        LAS: 0.125273849831
#        
#        Not this:
#        
#        Traceback (most recent call last):
#        File "test.py", line 41, in <module>
#        ...
#        NotImplementedError: Please implement shift!
#        
#        
#        """