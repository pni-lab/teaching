# Imports and Co
import pandas as pd
import plotly.io as pio
import plotly.figure_factory as ff

import plotly.offline as py #replaces import plotly.plotly as py
py.offline.init_notebook_mode()
import plotly.graph_objs as go
import plotly.express as px


# Set default renderer
pio.renderers.default = 'notebook+jupyterlab'  #  See [1]

# Set default template
pio.templates['slides'] = go.layout.Template(layout=dict(width=800, height=550))
pio.templates.default = 'plotly+slides'  # See [2]

#############################################################


def plot_scatter_with_regline(data, x, y, predicted=None, legend=("subject", "line")):
    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[x], y=data[y],
                             mode='markers', name=legend[0]))
    if predicted is None:
        predicted = data[x]
    fig.add_trace(go.Scatter(x=data[x], y=predicted,
                             mode='lines',
                             name=legend[1]))
    return fig


def plot_scatter_with_regpoints(data, x, y, predicted=None, legend=("subject", "prediction")):
    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[x], y=data[y],
                             mode='markers', name=legend[0]))
    if predicted is None:
        predicted = data[x]
    fig.add_trace(go.Scatter(x=data[x], y=predicted,
                             mode='markers',
                             name=legend[1]))
    return fig

