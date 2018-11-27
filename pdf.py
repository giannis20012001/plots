import pandas as pd
import plotly
import plotly.graph_objs as go

data_req = pd.read_csv(
    r'/home/lumi/Dropbox/unipi/paper_NVD_forcasting/distribution_fitting/PDF.csv',
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
    opacity=0.1
)

trace1 = go.Scatter(
    x=x,
    y=burr,
    mode='lines',
    name='burr'
)

trace2 = go.Scatter(
    x=x,
    y=dagum,
    mode='lines',
    name='dagum'
)

trace3 = go.Scatter(
    x=x,
    y=pearson_5_3P,
    mode='lines',
    name='pearson_5_3P'
)

data = [trace0, trace1, trace2, trace3]

# plotly.offline.plot(data, filename='pdf.html')
plotly.offline.plot(data, filename='pdf.html', image="svg")