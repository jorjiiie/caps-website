import json
import matplotlib.pyplot as plt
import seaborn as sns

f = open('data2.json')

data = json.load(f)
f.close()

bin_sz = 100 #number of pixels for heatmap width
x_width = 1900 # prediction width
y_width = 900 # prediction width
n = len(data)
def clamp(n,x,y):
    return int(max(x,min(n,y)))
x_bins = (x_width - 1) // bin_sz + 1
y_bins = (y_width - 1) // bin_sz + 1

bins = [[0 for i in range(x_bins)] for i in range(y_bins)]
for d in bins:
    print(d)
    

for d in data:
    xbin = clamp(d['xprediction'] / bin_sz, 0, x_bins-1)
    ybin = clamp(d['yprediction'] / bin_sz, 0, y_bins-1)
    bins[ybin][xbin] += 1/n


sns.set_theme()
plt.figure(figsize=(10,4))
heat_map = sns.heatmap(bins, linewidth=1, cmap="rocket_r")
plt.title("Heatmap")
plt.show()
