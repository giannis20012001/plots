import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_bins = 8
data_req = data = pd.read_csv('/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics/distribution_fitting/CDF.csv', sep=",")
#Different function: data_req = pd.read_table("/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics/distribution_fitting/CDF.csv", sep=",")
#To sort values: sorted_values = data_req.apply(lambda x: x.sort_values())

x = data_req.x
burr = data_req.Burr
dagum = data_req.Dagum
pearson53P = data_req.Pearson_5_3P

# plot the cumulative histogram
n, bins, patches = plt.hist(x.values, n_bins, density=True, histtype='step', cumulative=True, label='Sample')

plt.show()