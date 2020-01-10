from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app



style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Use the controls below to update your predicted exit destination, based on length of stay, 
        income at entry, total household members, and total contact services.
    
    """), 
    
    
    
    

    html.Div(id='prediction-content', style={'fontWeight':'bold'}), 

    html.Div([
        dcc.Markdown('###### Length of time homeless'), 
        dcc.Slider(
            id='length_homeless', 
            min=0,
            max=200,
            step=5,
            value=30, 
            marks={n: str(n) for n in range(0,200,5)}
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Income at Entry'), 
        dcc.Slider(
            id='entry_income', 
            min=0,
            max=2000, 
            step=200, 
            value=800, 
            marks={n: str(n) for n in range(0,2000,200)}
        ),
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Total Household Size'), 
        dcc.Slider(
            id='CaseMembers', 
            min=1, 
            max=10, 
            step=1, 
            value=3, 
            marks={n: str(n) for n in range(0,10,1)}
        ),  
    ], style=style),


])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('length_homeless)', 'value'),
     Input('entry_income', 'value'),
     Input('CaseMembers', 'value')])
def predict(length_homeless, entry_income, CaseMembers):

    df = pd.DataFrame(
        columns=['length_homeless', 'entry_income', 'CaseMembers'], 
        data=[[length_homeless, entry_income, CaseMembers]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred = pipeline.predict(df)[0]
    

    return f'{y_pred:.0f} interest rate predicted for 36 month Lending Club loan'
 
 
