from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import plotly.graph_objs as go

from app import app

x = load('model/x.joblib')
y = load('model/y.joblib')
z = load('model/z.joblib')

data = [
    go.Surface(
        z=z, 
        x=x, 
        y=y
    )
]
layout = go.Layout(
    title='Partial Dependence Plot',
    scene={'xaxis': {'title': 'Annual Income', 'showticklabels': True}, 
           'yaxis': {'title': 'Credit Score', 'showticklabels': True}, 
           'zaxis': {'title': 'Interest Rate', 'showticklabels': True}}, 
    width=800, 
    height=800
)
fig = go.Figure(data=data, layout=layout)

layout = [dcc.Markdown("""
### Explain

"""), 

dcc.Graph(id='explain-graph', figure=fig)
]