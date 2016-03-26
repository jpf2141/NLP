



from providedcode.transitionparser import TransitionParser
from providedcode.dependencygraph import DependencyGraph
import fileinput
import sys


if sys.argv[1]:
    model = sys.argv[1]
    tp = TransitionParser.load(model)

    for line in sys.stdin:
        sent = DependencyGraph.from_sentence(line)
        parsed = tp.parse([sent])
        parsed = parsed[0].to_conll(10)
        parsed = parsed.encode('utf-8')
        print parsed
        sys.stdout.flush()
else:
    print "Usage: cat englishfile | python parse.py english.model > englishfile.conll"