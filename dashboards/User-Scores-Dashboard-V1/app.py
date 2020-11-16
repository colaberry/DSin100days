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
from dash.dependencies import Output, Input, State
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

    
@app.callback( Output('user-score', 'children'),
                [Input('all-users-table', 'data_timestamp'),
                Input('all-users-table', 'active_cell')],
                [State('all-users-table', 'data')])
def get_active_cell_value (timestamp, active_cell, data):
    timestamp = "NA"
    active_cell_value = "NA"
    if active_cell:
        active_cell_value = str(data[active_cell['row']][active_cell['column_id']])
   # children = [active_cell_row_index, active_cell_column_index, active_cell_value] 
    return figures.user_scores(str(active_cell_value))

if __name__ == "__main__":
    app.run_server(debug=True)



