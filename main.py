"""
Aluno: Lucas Prado da Costa Burgos
lpcb@cin.ufpe.br
Projeto 2 - Algoritmos e Estruturas de dados(IF969)
28-10-2018
"""

from estruturas.corpus import Corpus
import cProfile
import os


pr = cProfile.Profile()
pr.enable()

a = Corpus('./dados/src/', 3)

print('-----------------------------------------terminou de fazer a arvore-------------------------------------------------')

path = './dados/susp/'

filelist = os.listdir(path)

for i in filelist[0:1]:
    if i.endswith(".txt"):
        docPath = str(path) + str(i)
        docs = a.verificarPlagio(docPath, 0.8)
        print('Documento: ', i, '\nPLAGIADOS: ', docs)



pr.disable()
pr.print_stats()