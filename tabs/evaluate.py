from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotly.tools import mpl_to_plotly
import seaborn as sns

from app import app

pipeline = load('model/pipeline.joblib')
history = pd.read_excel('model/n_alltime.xlsx')
X = history.drop(columns='perm_leaver')
y_pred_log = pipeline.predict(X)
y_pred = np.expm1(y_pred_log)

fig, ax = plt.subplots()
sns.distplot(history['perm_leaver'], hist=False, kde=True, ax=ax, label='Actual')
sns.distplot(y_pred, hist=False, kde=True, ax=ax, label='Predicted')
ax.set_title('Distribution of predictions is simpler and less spread than actuals')
ax.legend().set_visible(False)
plotly_fig = mpl_to_plotly(fig)
plotly_fig['layout']['showlegend'] = True

layout = [dcc.Markdown("""
### Evaluate

"""), 

dcc.Graph(id='evaluate-graph', figure=plotly_fig)
]