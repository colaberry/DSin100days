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

if __name__ == "__main__":
    app.run_server(debug=True)




