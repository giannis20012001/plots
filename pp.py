import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'C:\Users\lumi\Dropbox\Unipi\paper_NVD_forcasting\distribution_fitting\PDF.csv',
    skiprows=1,
    names=['x', 'P_empirical', 'Burr', 'Dagum', 'Pearson_5_3P'],
    sep=",")

x = data_req.x
p_empirical = data_req.P_empirical
burr = data_req.Burr
dagum = data_req.Dagum
pearson_5_3P = data_req.Pearson_5_3P

# Create traces
trace0 = go.Scatter(
    x=x,
    y=p_empirical,
    mode='lines',
    name='burr'
)

# trace1 = go.Scatter(
#     x=x,
#     y=burr,
#     name='burr',
#     line = dict(
#         color=('rgb(55, 128, 191)'),
#         width=3,
#         dash='dot')
# )

# trace2 = go.Scatter(
#     x=x,
#     y=dagum,
#     name='dagum',
#     line = dict(
#         color=('rgb(50, 171, 96)'),
#         width=3,
#         dash='dot')
# )

# trace3 = go.Scatter(
#     x=x,
#     y=pearson_5_3P,
#     name='pearson_5_3P',
#     line = dict(
#         color=('rgb(128, 0, 128)'),
#         width=3,
#         dash='dot')
# )

# data = [trace0, trace1, trace2, trace3]
data = [trace0]

layout = go.Layout(
    title='P-P Plot',
    xaxis=dict(
        title='P(Empirical)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='F(Model)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='pp.html')
# plotly.offline.plot(data, filename='pp.html', image="svg")