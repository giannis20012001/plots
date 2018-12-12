import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'C:\Users\lumi\Dropbox\Unipi\paper_NVD_forcasting\distribution_fitting\various_prolt_data.csv',
    skiprows=1,
    names=['published_datetime', 'score'],
    sep=",")

data_req.score = data_req.score.astype(float)
x = pd.Series([pd.to_datetime(date) for date in data_req.published_datetime])
y = data_req.score

# Create trace
trace = go.Scatter(
    x = x,
    y = y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
plotly.offline.plot(data, filename='scatter_plot.html', image="svg")