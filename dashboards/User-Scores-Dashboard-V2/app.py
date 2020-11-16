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
    Output(component_id='user-completion', component_property='children'),
    [Input(component_id='input-username', component_property='value'),
     Input(component_id='input-coursename', component_property='value')]
)
def update_user_completion_div(input_username,input_coursename):
    data = figures.user_completion_table(str(input_username),str(input_coursename))
    if data is not None:
        return data
    else:
        return "No user found"

@app.callback(
    Output(component_id='user-course-details', component_property='children'),
    [Input(component_id='input-username', component_property='value'),
     Input(component_id='input-coursename', component_property='value')]
)
def update_user_course_details_div(input_username,input_coursename):
    data = figures.course_details_table(str(input_username),str(input_coursename))
    if data is not None:
        return data
    else:
        return "No user found"    

if __name__ == "__main__":
    app.run_server(debug=True)



