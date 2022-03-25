import json
import matplotlib.pyplot as plt
import matplotlib.dates
import seaborn as sns

f = open('data2.json')

data = json.load(f)
f.close()

xmax = 0
ymax = 0
ymin = 1000
xmin = 1000
for d in data:
    xmax=max(xmax, d['xprediction'])
    ymax=max(ymax,d['yprediction'])
    xmin=min(xmin,d['xprediction'])
    ymin=min(ymin,d['yprediction'])

print(xmin, xmax)
print(ymin,ymax)
