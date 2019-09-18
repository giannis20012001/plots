import pandas as pd
import plotly
import plotly.graph_objs as go

plotly.io.orca.config.executable = '/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/orca-1.2.1-x86_64.AppImage'
data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/p-p_plot.csv',
    skiprows=1,
    names=['original_x', 'x', 'P_empirical', 'Burr', 'Dagum', 'Pearson_5_3P'],
    sep=",")

x = data_req.x
original_x = data_req.original_x
p_empirical = data_req.P_empirical
burr = data_req.Burr
dagum = data_req.Dagum
pearson_5_3P = data_req.Pearson_5_3P

# Create traces
trace0 = go.Scatter(
    x=x,
    y=x,
    mode='lines',
    name='P'
)

trace1 = go.Scatter(
    x=p_empirical,
    y=burr,
    name='Burr',
    line = dict(
        color=('rgb(55, 128, 191)'),
        width=3,
        dash='dot')
)

trace2 = go.Scatter(
    x=p_empirical,
    y=dagum,
    name='Dagum',
    line = dict(
        color=('rgb(50, 171, 96)'),
        width=3,
        dash='dot')
)

trace3 = go.Scatter(
    x=p_empirical,
    y=pearson_5_3P,
    name='Pearson 5(3P)',
    line = dict(
        color=('rgb(128, 0, 128)'),
        width=3,
        dash='dot')
)

data = [trace0, trace1, trace2, trace3]
# data = [trace0]

layout = go.Layout(
    #title='P-P Plot',
    xaxis=dict(
        title='P(Empirical)',
        ticks="inside",
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='P(Model)',
        ticks="inside",
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    # legend=dict(orientation="h")
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(size=18),
    legend=dict(orientation="v",x=.75, y=0)
)

fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='p-p_plot.html')
# plotly.offline.plot(fig, filename='p-p_plot.html', image="svg")
fig.write_image("p-p_plot.pdf")