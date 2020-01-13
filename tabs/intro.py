from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

This webapp will let you predict exit destinations of a family based off of several aspects that typically present when new guests arrive at the shelter.  Please use the sliders to match the self-attested information given by the head of household  
"""), 

html.Img(src='/assets/fpspokane.png', style={'width':'100%'})]
