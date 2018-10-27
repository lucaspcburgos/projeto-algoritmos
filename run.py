from corpus.corpus import Corpus
"""
import cProfile
import re

cProfile.run('re.compile("foo|bar")')
"""
a = Corpus('./teste/', 3)
docs = a.verificarPlagio('teste2.txt', 0.8)
print('plágios: ',docs)

