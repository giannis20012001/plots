import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'C:\Users\lumi\Dropbox\Unipi\paper_NVD_forcasting\distribution_fitting\Cumulative_vulnerability_scores_regression_modeling.csv',
    skiprows=1,
    names=['published_datetime_week', 'cumulative_scores', 'modeled_cumulative_scores'],
    sep=",")

data_req.cumulative_scores = data_req.cumulative_scores.astype(float)
data_req.modeled_cumulative_scores = data_req.modeled_cumulative_scores.astype(float)
x = pd.Series([pd.to_datetime(date) for date in data_req.published_datetime_week])
y = data_req.cumulative_scores

# Create trace 0
trace0 = go.Scatter(
    x = x,
    y = y,
    name='High 2014'
)

y = data_req.modeled_cumulative_scores

# Create trace 1
trace1 = go.Scatter(
    x = x,
    y = y,
    name='High 2014'
)

data = [trace0, trace1]

# Edit the layout
layout = dict(title = 'Average High and Low Temperatures in New York',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Temperature (degrees F)'),
              )

fig = dict(data=data, layout=layout)

# Plot and embed in ipython notebook!
plotly.offline.plot(fig, filename='cvsrm.html', image="svg")