import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
from data import(
    queries,
    )
from graphs import(
    figures,
    )


def create_layout(app):
    return html.Div([
    html.H1(
        'User Scorecard',
        style={
            'textAlign': 'center',
            }
        ),
    html.Br(),
    html.Br(),
    
    html.Div(["Enter a Username: ",
              dcc.Input(id='input-username', value='', type='text')]),
    html.Br(),
    html.Div(["Select a Course: ",
              dcc.Dropdown(
                  id = 'input-coursename',
                  options= queries.get_courses(),
                  value='Data Science - I'
        )]),
    html.Br(),
    html.H4('User Course Completion',
        style={'textAlign': 'left',}
        ),
    html.Div(id='user-completion'),
    html.Br(),
    html.H4('Course Details',
        style={'textAlign': 'left',}
        ),
    html.Div(id='user-course-details'),
])






