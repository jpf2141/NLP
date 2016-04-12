import numpy as np
import json
import gensim
from gensim.models import Word2Vec


def train(sentences):
    model = Word2Vec(size=100, window=5, min_count=1)
    model.build_vocab(sentences)
    alpha, min_alpha, passes = (0.025, 0.001, 20)
    alpha_delta = (alpha - min_alpha) / passes
    
    for epoch in range(passes):
        model.alpha, model.min_alpha = alpha, alpha
        model.train(sentences)
        
        print('completed pass %i at alpha %f' % (epoch + 1, alpha))
        alpha -= alpha_delta
        
        np.random.shuffle(sentences)
    return model


with open("hist_split.json") as file:
    sentence_list = []
    file = file.read()
    trainingData = json.loads(file)['train']
    for item in trainingData:
        sentence = []
        for line in item[0]:
            if line[0] == None:
                sentence.append("None")
            else:
                sentence.append(line[0])
        sentence_list.append(sentence)

    model = train(sentence_list)
    model.save("model")