import sys
from maximaze import Maximaze

file = sys.argv[1]
print('\nARQUIVO: ', file)

try:
    f = open(file)
    data = f.read().splitlines()

except Exception as e:
    print(e)

w = int(data[0])
weights = []
values = []
acuWeight = 0

for d in data[1:]:
    d = d.split(',')
    weights.append(int(d[0]))
    values.append(int(d[1]))

totalData = len(weights)

a = Maximaze(maxWeight=w, maxItems=totalData, itemsWeights=weights, itemsValues=values)

for w in a.items:
    acuWeight += w[1]

print('\nÍTENS SELECIONADOS(valor/peso):\n', a.items)
print('\nVALOR MÁXIMO:', a.value)
print('\nPESO ACUMULADO: ', acuWeight, '\n')
