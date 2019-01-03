import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_&_distribution_fitting/Normal_Probability_Plot.csv',
    skiprows=1,
    names=['percentile', 'weekly_score_probability_output'],
    sep=",")

data_req.percentile = data_req.percentile.astype(float)
data_req.weekly_score_probability_output = data_req.weekly_score_probability_output.astype(float)
x = data_req.percentile
y = data_req.weekly_score_probability_output

# Create trace 0
trace0 = go.Scatter(
    x = x,
    y = y,
    mode='lines',
    name='Normal Probability Plot'
)

data = [trace0]

# Edit the layout
layout = dict(title = 'Normal Probability Plot',
              xaxis = dict(title = 'Sample Percentile'),
              yaxis = dict(title = 'Weekly Score Probability Output'),
              legend=dict(orientation="h")
              )

fig = dict(data=data, layout=layout)
#plotly.offline.plot(fig, filename='npp.html')
plotly.offline.plot(fig, filename='npp.html', image="svg")