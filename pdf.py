import pandas as pd
import plotly
import plotly.graph_objs as go

plotly.io.orca.config.executable = '/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/orca-1.2.1-x86_64.AppImage'
data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/pics_and_distribution_fitting/PDF.csv',
    skiprows = 1,
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
    name='Histogram'
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

data = [trace0, trace1, trace2, trace3]

layout = go.Layout(
    # title='Probability Density Function',
    xaxis=dict(
        title='x',
        ticks="inside",
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='f(x)',
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
    legend=dict(orientation="v",x=.75, y=1)
)

fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='pdf.html')
# plotly.offline.plot(fig, filename='pdf.html', image="svg")
fig.write_image("pdf.pdf")