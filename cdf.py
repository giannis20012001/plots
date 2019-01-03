import plotly
import pandas as pd
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_&_distribution_fitting/CDF.csv',
    skiprows=1,
    names=['Initial_data', 'x', 'Burr', 'Dagum', 'Pearson_5_3P'],
    sep=",")

initial_data = data_req.Initial_data
initial_data.dropna()
x = data_req.x
burr = data_req.Burr
dagum = data_req.Dagum
pearson_5_3P = data_req.Pearson_5_3P

# Create traces
trace0 = go.Histogram(
    histfunc="count",
    histnorm="probability density",
    x=initial_data,
    xbins=dict(
        start='1.9',
        end='10',
        size='1.0125'),
    autobinx=False,
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgba(17, 157, 255, 0.5)',
            width=1.5,
        )
    ),
    opacity=0.5,
    cumulative=dict(enabled=True),
    name='Sample'
)

trace1 = go.Scatter(
    x=x,
    y=burr,
    mode='lines',
    name='Burr'
)

trace2 = go.Scatter(
    x=x,
    y=dagum,
    mode='lines',
    name='Dagum'
)

trace3 = go.Scatter(
    x=x,
    y=pearson_5_3P,
    mode='lines',
    name='Pearson 5(3P)'
)

# data = [go.Histogram(
#     histfunc="count",
#     histnorm="probability density",
#     x=initial_data,
#     xbins=dict(
#         start='1',
#         end='10',
#         size='1.2'),
#     autobinx=False,
#     cumulative=dict(enabled=True))]

# data = [go.Histogram(
#     histfunc="count",
#     histnorm="probability density",
#     x=initial_data,
#     nbinsx=9,
#     autobinx=False,
#     cumulative=dict(enabled=True))]

# data = [go.Histogram(
#     histfunc="count",
#     histnorm="probability density",
#     x=initial_data,
#     nbinsx=9,
#     cumulative=dict(enabled=True)),
#     trace0,
#     trace1,
#     trace2]

data = [trace0, trace1, trace2, trace3]

layout = go.Layout(
    title='Cumulative Distribution Function',
    xaxis=dict(
        title='x',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='F(x)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    legend=dict(orientation="h")
)

fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='cdf.html')
plotly.offline.plot(fig, filename='cdf.html', image="svg")
