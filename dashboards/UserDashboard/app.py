import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd 
import plotly.express as px
import dash_table
import json
from data import(
    queries,
    )
from graphs import(
    figures,
    )
from pages import(
    homePage
    )

external_stylesheets = ['C:/Users/Rohit/ColaberryDashboard/UserDashboard/assets'] 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
          homePage.create_layout(app)
])

@app.callback(
    Output('click-data-users-by-week', 'children'),
    [Input('new_users-by-week', 'clickData')])
def display_users_by_week_table(clickData):
    # s = json.dumps(clickData)
    if clickData is not None and "points" in clickData:

        x = clickData["points"][0]["x"]
        return figures.generate_users_by_week_table(x)
    return 0

@app.callback(
    Output('click-data-users-by-day', 'children'),
    [Input('user-by-day-graph', 'clickData')])
def display_users_by_day_table(clickData):
    # s = json.dumps(clickData)
    if clickData is not None and "points" in clickData:

        x = clickData["points"][0]["x"]
        return figures.generate_users_by_day_table(x)
    return 0

# @app.callback(
#     Output('click-data-unique-users-visiting-notebooks-by-day', 'children'),
#     [Input('user-by-day-visting-notebooks-graph', 'clickData')])
# def display_unique_users_visiting_notebooks_by_day_table(clickData):
#     if clickData is not None and "points" in clickData:
#         x = clickData["points"][0]["x"]
#         return figures.generate_unique_users_visiting_notebooks_by_day_table(x)
#     return 0

if __name__ == "__main__":
    app.run_server(debug=True)

# app.layout = html.Div([  
#     html.H1(
#         'Refactored Metrics',
#         style={
#             'textAlign': 'center',
#             }
#         ),
    
#     html.Div([dcc.Graph(
#         id='new_users-by-week',
#         figure=figures.new_users_by_week_bar_graph()
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

#     html.Div(
#         id='click-data',
#         style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'},
#         ),
        #, style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
    # html.Div([
    # figures.generate_table('2020-09-28')
    # ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
    # html.Div([
    #       dash_table.DataTable(
    #       id='new-users-table',
    #       columns=[{"name": i, "id": i} for i in queries.new_users_list().columns],
    #       data=new_users_list.to_dict('records'),   
    #   )
    #       ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

#     html.Div([dcc.Graph(
#         id='user-by-day-visting-notebooks-graph',
#         figure=figures.users_by_day_line_graph()
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
#     html.Div([dcc.Graph(
#         id='user-by-day-graph',
#         figure=figures.users_by_day_bar_graph()
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
#       html.Div([dcc.Graph(
#         id='user-activity-per-hour-graph',
#         figure=figures.user_activity_per_hour()
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
      
# ])
                

# if __name__ == "__main__":
#     app.run_server(debug=True)


