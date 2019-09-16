import pandas as pd
import plotly
import plotly.graph_objs as go

plotly.io.orca.config.executable = '/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/orca-1.2.1-x86_64.AppImage'
data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/VDM_Regression_Analysis/published_datetime_week_Residual_Plot.csv',
    skiprows=1,
    names=['published_datetime_week', 'residuals'],
    sep=",")

data_req.residuals = data_req.residuals.astype(float)
x = pd.to_datetime(data_req['published_datetime_week'], format="%m/%d/%Y")
# x = pd.Series([pd.to_datetime(date) for date in data_req.published_datetime_week]) # Alternative way
y = data_req.residuals

# Create trace 0
trace0 = go.Scatter(
    x = x,
    y = y,
    mode='lines',
    name='Residuals of Published Datetimes'
)

data = [trace0]

# Edit the layout
layout = dict(# title = 'Residual Plot of Published Datetimes',
    xaxis = dict(title = 'Dates'),
    yaxis = dict(title = 'Residuals'),
    # legend=dict(orientation="h")
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(size=18),
    legend=dict(orientation="v",x=.75, y=0)
)

# fig = dict(data=data, layout=layout)
fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='pdwrp.html')
# plotly.offline.plot(fig, filename='pdwrp.html', image="svg")
fig.write_image("pdwrp.pdf")