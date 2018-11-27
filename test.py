import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/distribution_fitting/CDF.csv',
    skiprows = 1,
    names=['Initial_data', 'x', 'Burr', 'Dagum', 'Pearson_5_3P'],
    sep=",")

cdf_data = data_req.x
burr = data_req.Burr
dagum = data_req.Dagum
pearson_5_3P = data_req.Pearson_5_3P
initial_data = data_req.Initial_data
initial_data.dropna()

# Create traces
trace0 = go.Scatter(
    x = burr,
    mode = 'lines',
    name = 'burr'
)
trace1 = go.Scatter(
    x = dagum,
    mode = 'lines',
    name = 'dagum'
)
trace2 = go.Scatter(
    x = pearson_5_3P,
    mode = 'lines',
    name = 'pearson_5_3P'
)

data = [go.Histogram(
    histfunc="count",
    histnorm="probability density",
    x=initial_data,
    xbins=dict(
        start='1.9',
        end='10',
        size='1.1'),
    autobinx=False,
    cumulative=dict(enabled=True))]

# data = [go.Histogram(
#     histfunc="count",
#     histnorm="probability density",
#     x=initial_data,
#     nbinsx=9,
#     autobinx=False,
#     cumulative=dict(enabled=True))]

# data = [trace0, trace1, trace2]

# data = [go.Histogram(
#     histfunc="count",
#     histnorm="probability density",
#     x=cdf_data,
#     nbinsx=10,
#     cumulative=dict(enabled=True)),
#     trace0,
#     trace1,
#     trace2]

plotly.offline.plot(data, filename='cumulativeHistogram.html')