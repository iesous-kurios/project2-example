from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

# import plotly.graph_objs as go
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.ensemble.partial_dependence import partial_dependence
# from sklearn.datasets.california_housing import fetch_california_housing

# cal_housing = fetch_california_housing()

# # split 80/20 train-test
# X_train, X_test, y_train, y_test = train_test_split(cal_housing.data,
#                                                     cal_housing.target,
#                                                     test_size=0.2,
#                                                     random_state=1)
# names = cal_housing.feature_names

# print("Training GBRT...")
# clf = GradientBoostingRegressor(n_estimators=100, max_depth=4,
#                                 learning_rate=0.1, loss='huber',
#                                 random_state=1)
# clf.fit(X_train, y_train)
# print(" done.")

# target_feature = (1, 5)
# pdp, axes = partial_dependence(clf, target_feature,
#                                X=X_train, grid_resolution=50)
# XX, YY = np.meshgrid(axes[0], axes[1])
# Z = pdp[0].reshape(list(map(np.size, axes))).T

# surf = go.Surface(x=XX, y=YY, z=Z)

# layout = go.Layout(title='Partial dependence of house value on median age and '
#                           'average occupancy',
#                    scene=dict(xaxis=dict(title=names[target_feature[0]],
#                                          showticklabels=False),
#                               yaxis=dict(title=names[target_feature[1]],
#                                          showticklabels=False),
#                               zaxis=dict(title='Partial dependence',
#                                          showticklabels=False))
#                    )
# fig = go.Figure(data = [surf], layout=layout)


layout = [dcc.Markdown("""
### Explain

This isn't Lending Club data, just an example of 
[partial dependence plots in Plotly](https://plot.ly/scikit-learn/plot-partial-dependence/)"""), 

# dcc.Graph(id='explain-graph', figure=fig)
]