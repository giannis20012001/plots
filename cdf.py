import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_bins = 8
data_req = pd.read_csv('C:\Users\lumi\Dropbox\Unipi\paper_NVD_forcasting\distribution_fitting\CDF.csv', skiprows = 1, names=['x', 'Burr', 'Dagum', 'Pearson_5_3P'], sep=",")
#Different function: data_req = pd.read_table("/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics/distribution_fitting/CDF.csv", sep=",")
#To sort values: sorted_values = data_req.apply(lambda x: x.sort_values())

x = data_req.x
burr = data_req.Burr
dagum = data_req.Dagum
pearson_5_3P = data_req.Pearson_5_3P
fig, ax = plt.subplots()

# plot the cumulative histogram
#n, bins, patches = plt.hist(x.values, n_bins, density=True, histtype='step', cumulative=True, label='Sample')
n, bins, patches = plt.hist(x.values, n_bins, density=1, histtype='step', cumulative=True, label='Sample')

#ax.plot(bins, burr, dagum, pearson_5_3P)
ax.plot(bins)
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()