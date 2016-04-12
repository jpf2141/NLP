from dependencyRNN import DependencyRNN
import sklearn
from sklearn.manifold import TSNE
import matplotlib.pyplot as plot
import numpy as np


embedding = DependencyRNN.load("random_init.npz")
answerEmbedding = embedding.answers


answers = []
for item in answerEmbedding:
    answers.append(answerEmbedding[item])


X = np.asarray(answers)
tsne = TSNE(n_components=2, perplexity=30.0)
X_reduced = tsne.fit_transform(X)
xaxis= []
yaxis = []
for x, y in X_reduced:
    xaxis.append(x)
    yaxis.append(y)


answers = []
for item in answerEmbedding:
    answers.append(item)


blank, axes = plot.subplots()
axes.scatter(xaxis, yaxis)
for index in range(len(answers)):
    axes.annotate(answers[index], (xaxis[index], yaxis[index]))


plot.show()