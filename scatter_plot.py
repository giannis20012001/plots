import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_&_distribution_fitting/scatter_plot_original.csv',
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
    mode = 'markers',
    name='Score (original)'
)

data = [trace]

layout = go.Layout(
    title='Score (original)',
    xaxis=dict(
        title='Dates',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        ),
        showline=True
    ),
    yaxis=dict(
        title='Score',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        ),
        showline=True
    )
)

fig = go.Figure(data=data, layout=layout)

# Plot and embed in ipython notebook!
plotly.offline.plot(fig, filename='scatter_plot.html', image="svg")