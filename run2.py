from corpus.corpus import Corpus
import cProfile

pr = cProfile.Profile()
pr.enable()

a = Corpus('./dados/src/', 3)
docs = a.verificarPlagio('./dados/susp/suspicious-document00005.txt', 0.8)
print('plágios: ', docs)

pr.disable()
pr.print_stats()