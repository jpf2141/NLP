from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition
import time
import random



if __name__ == '__main__':
    traindata = dataset.get_swedish_train_corpus().parsed_sents()

#generate random sampling of training data
    sample_size = 10
    time_seed = lambda: int(round(time.time() * 1000))
    random.seed(time_seed)
    train_sample = random.sample(traindata, sample_size)


    try:

        print "0"
        tp = TransitionParser(Transition, FeatureExtractor)
        print "1"
        tp.train(train_sample)
        print "2"
        # tp.save('swedish.model')
        print "3"

        labeleddata = dataset.get_swedish_dev_corpus().parsed_sents()
        blinddata = dataset.get_swedish_dev_blind_corpus().parsed_sents()
        tp = TransitionParser.load('badfeatures.model')

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
