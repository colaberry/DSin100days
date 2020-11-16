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
        'Refactored Metrics',
        style={
            'textAlign': 'center',
            }
        ),
    
    html.H4(
        'New Users by Week',
        style={
            'textAlign': 'left',
            }
        ),
    
    html.Div([dcc.Graph(
        id='new_users-by-week',
        figure=figures.new_users_by_week_bar_graph()
    )], style={'width': '100%', 'display': 'inline-block', 'padding': '0 10'}),
    
    html.Div(
        id='click-data-users-by-week',
        style={'width': '100%', 'display': 'inline-block', 'padding': '0 10'},
        ),
    
    html.Br(),
    
    html.H4(
        'Number of Users by Day',
        style={
            'textAlign': 'left',
            }
        ),
    
    html.Div([dcc.Graph(
        id='user-by-day-graph',
        figure=figures.users_by_day_bar_graph()
    )], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div(
        id='click-data-users-by-day',
        style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'},
        ),
    
    html.H4(
        'Unique Users Visiting Notebooks',
        style={
            'textAlign': 'left',
            }
        ),
    
    html.Div([dcc.Graph(
        id='user-by-day-visting-notebooks-graph',
        figure=figures.users_visiting_notebooks_line_graph()
    )], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    
    html.Div(
        id='click-data-unique-users-visiting-notebooks-by-day',
        style={'width': '100%', 'display': 'inline-block', 'padding': '0 10'},
        ),
    
    html.H4(
        'User Activity per Hour',
        style={
            'textAlign': 'left',
            }
        ),
    
    html.Div([dcc.Graph(
        id='user-activity-per-hour-graph',
        figure=figures.user_activity_per_hour()
    )], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
])




# app.layout = html.Div([
#     html.H1(
#         'Refactored Metrics',
#         style={
#             'textAlign': 'center',
#             }
#         ),
    
#      html.Div([dcc.Graph(
#         id='new_users-by-week',
#         figure=fig1
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

#     html.Div([dcc.Graph(
#         id='user-by-day-visting-notebooks-graph',
#         figure=fig2
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
#     html.Div([dcc.Graph(
#         id='user-by-day-graph',
#         figure=fig3
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
#      html.Div([dcc.Graph(
#         id='user-activity-per-hour-graph',
#         figure=fig4
#     )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
      
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

