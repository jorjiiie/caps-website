import json
import matplotlib.pyplot as plt
import matplotlib.dates
import seaborn as sns

f = open('09042022.json')

data = json.load(f)
f.close()

num_bins = 10
n = len(data)
def clamp(n, nbins):
    return int(max(0, min(nbins-1, n)))
# 10 bins in both directions
bins = [[0 for i in range(num_bins)] for i in range(num_bins)]
print(bins)

# 1000 -> width = 50
for d in data:
    xbin = clamp(d['xprediction']/1920 * num_bins, num_bins)
    ybin = clamp(d['yprediction']/900 * num_bins, num_bins)
    bins[xbin][ybin] += 1/n
    print(xbin, ybin)

print(bins)
    
print(len(data))

sns.set_theme()
# 3. Plot the heatmap
plt.figure(figsize=(4,4))
heat_map = sns.heatmap( bins, linewidth = 1 , annot = False, cmap="rocket_r")
plt.title( "Eyetracking heatmap" )
plt.show()
