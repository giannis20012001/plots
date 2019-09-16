import pandas as pd
import plotly
import plotly.graph_objs as go

plotly.io.orca.config.executable = '/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/orca-1.2.1-x86_64.AppImage'
data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/VDM_Regression_Analysis/Normal_Probability_Plot.csv',
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
layout = dict(# title = 'Normal Probability Plot',
    xaxis = dict(title = 'Sample Percentile'),
    yaxis = dict(title = 'Weekly Score Probability Output'),
    # legend=dict(orientation="h")
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(size=18),
    legend=dict(orientation="v",x=.75, y=0)
)

# fig = dict(data=data, layout=layout)
fig = go.Figure(data=data, layout=layout)
#plotly.offline.plot(fig, filename='npp.html')
# plotly.offline.plot(fig, filename='npp.html', image="svg")
fig.write_image("npp.pdf")