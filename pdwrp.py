import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_&_distribution_fitting/published_datetime_week_Residual_Plot.csv',
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
layout = dict(title = 'Residual Plot of Published Datetimes',
              xaxis = dict(title = 'Dates'),
              yaxis = dict(title = 'Residuals'),
              )

fig = dict(data=data, layout=layout)
# plotly.offline.plot(fig, filename='pdwrp.html')
plotly.offline.plot(fig, filename='pdwrp.html', image="svg")