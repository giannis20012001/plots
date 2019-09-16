import pandas as pd
import plotly
import plotly.graph_objs as go

plotly.io.orca.config.executable = '/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/orca-1.2.1-x86_64.AppImage'
data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/VDM_Regression_Analysis/Cumulative_vulnerability_scores_regression_modeling.csv',
    skiprows=1,
    names=['published_datetime_week', 'cumulative_scores', 'modeled_cumulative_scores'],
    sep=",")

data_req.cumulative_scores = data_req.cumulative_scores.astype(float)
data_req.modeled_cumulative_scores = data_req.modeled_cumulative_scores.astype(float)
x = pd.to_datetime(data_req['published_datetime_week'], format="%m/%d/%Y")
# x = pd.Series([pd.to_datetime(date) for date in data_req.published_datetime_week]) # Alternative way
y = data_req.cumulative_scores
z = data_req.modeled_cumulative_scores

# Create trace 0
trace0 = go.Scatter(
    x = x,
    y = y,
    mode='lines',
    name='Cumulative Scores'
)

y = data_req.modeled_cumulative_scores

# Create trace 1
trace1 = go.Scatter(
    x = x,
    y = y,
    mode='lines',
    name='Modeled Cumulative Scores'
)

data = [trace0, trace1]

# Edit the layout
layout = dict(# title = 'Cumulative Vulnerability Scores Regression Modeling',
    xaxis = dict(title = 'Dates'),
    yaxis = dict(title = 'Cumulative Score'),
    # legend=dict(orientation="h")
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(size=18),
    legend=dict(orientation="v",x=.75, y=0)
)

# fig = dict(data=data, layout=layout)
fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='cvsrm.html')
# plotly.offline.plot(fig, filename='cvsrm.html', image="svg")
fig.write_image("cvsrm.pdf")