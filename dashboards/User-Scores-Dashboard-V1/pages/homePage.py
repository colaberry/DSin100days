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
    
    html.Div(
        id='all-users',
        children=figures.all_users_scores()
    ),
    
    html.Br(),
    html.Br(),    
    html.Br(),
    html.Br(),
    
    # html.Div(["Enter a Username: ",
    #           dcc.Input(id='input-username', value='', type='text')]),
    html.Br(),
    html.Br(),

    html.Div(id='user-score'),
])






