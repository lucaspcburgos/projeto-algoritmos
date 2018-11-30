from maximaze import Maximaze

w = 500
weights = [30, 45, 2345, 457, 45, 235, 47, 346, 346, 2456, 45, 3456]
values = [425, 1241, 7635, 986, 125, 856, 413, 4356, 673, 1234, 2345, 234]
pro = len(weights)

a = Maximaze(maxWeight=w, maxItems=pro, itemsWeights=weights, itemsValues=values)
print(a.items)
print(a.value)