from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from joblib import load
import plotly.graph_objs as go
import pandas as pd 
from app import app

x = load('model/x.joblib')
y = load('model/y.joblib')
z = load('model/z.joblib')

race_breakdown = pd.read_excel('assets/racebreakdown.xlsx')

fig2 = go.Figure(data=[
    go.Bar(name='Percent of Total Served', x=race_breakdown['Race'], y=race_breakdown['Percent of Total Served']),
    go.Bar(name='% with Perm Exit', x=race_breakdown['Race'], y=race_breakdown['Percent that had Exit to Perm'])
])
# Change the bar mode
fig2.update_layout(barmode='group')

data = [
    go.Surface(
        z=z, 
        x=x, 
        y=y
    )
]
layout = go.Layout(
    title='Partial Dependence Plot',
    scene={'xaxis': {'title': 'Income at Entry', 'showticklabels': False}, 
           'yaxis': {'title': 'Length of Time Homeless', 'showticklabels': False}, 
           'zaxis': {'title': 'Probability of Exit to Permanent Housing', 'showticklabels': False}}, 
    width=800, 
    height=800
)
fig = go.Figure(data=data, layout=layout)

layout = [dcc.Markdown("""
### Explain

"""), 


dcc.Markdown("""
### Feature Importances

This plot shows the top 20 features that had the most impact on the accuracy of my model
"""), 
html.Img(src='/assets/testplot2.png', style={'width':'100%'}),


dcc.Markdown("""
### Races and Exits to Permanent Housing

This plot presents Races as percent of total guests served and what percent of that race had an exit to Permanent Housing
"""), 

dcc.Graph(id='explain-graph', figure=fig2),


dcc.Markdown("""
### Shapley Plot

This plot shows the average of the marginal contributions across all permutations.
SHAP values can show how much each predictor contributes, either positively or negatively, to the target variable ( in this case; exit to permanent housing)
"""), 
html.Img(src='/assets/shap.png', style={'width':'100%'}),

html.Img(src='/assets/agebreakdown2.png', style={'width':'100%'}),
html.Img(src='/assets/racebreakdown2.png', style={'width':'100%'}),
html.Img(src='/assets/real_ethnicity2.png', style={'width':'100%'})



]
