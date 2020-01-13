import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash
from joblib import load
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

pipeline = load('model/pipeline.joblib')

from app import app

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Use the controls below to predict exit destination of a client based off of features which proved to have high significance in my prediction model
    
    """), 

    
dbc.Col(
    [


        html.H2('Exit To Permanent Housing', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        
        
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Income at Entry'), 
        dcc.Slider(
            id='entry_income', 
            min=0, 
            max=3000, 
            step=100, 
            value=0,
            marks={n: str(n) for n in range(0,3000,100)}, 
            className='mb-5', 
        ), 
        html.Div(id='slider-output-container'),

        dcc.Markdown('#### Length of Time Homeless in days'), 
        dcc.Slider(
            id='length_homeless', 
            min=0, 
            max=400, 
            step=10, 
            value=0,
            marks={n: str(n) for n in range(0,400,10)}, 
            className='mb-5', 
        ), 

        html.Div(id='slider-output-container'),
        
        dcc.Markdown('#### Total HouseHold Size'), 
        dcc.Slider(
            id='CaseMembers', 
            min=1, 
            max=10, 
            step=1, 
            value=1,
            marks={n: str(n) for n in range(1,10,1)}, 
            className='mb-5', 
        ), 

        html.Div(id='slider-output-container'),

        dcc.Markdown('#### Age at Enrollment'), 
        dcc.Slider(
            id='Age_at_Enrollment', 
            min=18, 
            max=65, 
            step=1, 
            value=25,
            marks={n: str(n) for n in range(18,65,1)}, 
            className='mb-5', 
        ), 
        html.Div(id='slider-output-container'),

    ],
    md=4,
)
])
dbc.Col(
    [
        html.H2('Exit To Permanent Housing', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd



@app.callback(
    dash.dependencies.Output('prediction-content', 'children'),
    [dash.dependencies.Input('entry_income', 'value'), dash.dependencies.Input('length_homeless', 'value'), 
    dash.dependencies.Input('CaseMembers', 'value'), dash.dependencies.Input('Age_at_Enrollment', 'value')],
)
def predict(entry_income, length_homeless, CaseMembers, Age_at_Enrollment):
    df = pd.DataFrame(
        columns=['CaseMembers','3.2_Social_Security_Quality', '3.3_Birthdate_Quality',
       'Age_at_Enrollment', '3.4_Race', '3.5_Ethnicity', '3.6_Gender',
       '3.7_Veteran_Status', '3.8_Disabling_Condition_at_Entry',
       '3.917_Living_Situation', 'length_homeless',
       '3.917_Times_Homeless_Last_3_Years', '3.917_Total_Months_Homeless_Last_3_Years', 
       'V5_Last_Permanent_Address', 'V5_State', 'V5_Zip', 'Municipality_(City_or_County)',
       '4.1_Housing_Status', '4.4_Covered_by_Health_Insurance', '4.11_Domestic_Violence',
       '4.11_Domestic_Violence_-_Currently_Fleeing_DV?', 'Household_Type', 
       'R4_Last_Grade_Completed', 'R5_School_Status',
       'R6_Employed_Status', 'R6_Why_Not_Employed', 'R6_Type_of_Employment',
       'R6_Looking_for_Work', 'entry_income',
       '4.3_Non-Cash_Benefit_Count', 'Barrier_Count_at_Entry',
       'Chronic_Homeless_Status', 'Under_25_Years_Old',
       '4.10_Alcohol_Abuse_(Substance_Abuse)', '4.07_Chronic_Health_Condition',
       '4.06_Developmental_Disability', '4.10_Drug_Abuse_(Substance_Abuse)',
       '4.08_HIV/AIDS', '4.09_Mental_Health_Problem',
       '4.05_Physical_Disability'
          ], 
        data=[[CaseMembers, np.NaN, np.NaN, Age_at_Enrollment, 
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, length_homeless, 
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, entry_income, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN,
        np.NaN, np.NaN, np.NaN, np.NaN, np.NaN]]
    )
    
    y_pred = pipeline.predict(df)[0]
    
    if y_pred == 0:
        return f'This example returned a {y_pred:.0f} which indicates that the client is not likely to exit to Perm Housing'
    else:    
        return f'This example returned a {y_pred:.0f} which indicates that the client is likely to exit to Permanent housing'  