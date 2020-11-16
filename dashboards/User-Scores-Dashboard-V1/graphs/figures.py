import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd 
import plotly.express as px
from data import(
    queries,
    )

def user_scores(input_value):
    dataframe = queries.get_user_score(input_value)
    return dash_table.DataTable(
        id='user_score-table',
        columns=[{"name": "Username", "id": "username"}
                 ,{"name": "First Name", "id": "first_name"}
                 ,{"name": "Last Name", "id": "last_name"}
                 ,{"name": "Email", "id": "email"}
                 ,{"name": "Course ID", "id": "course_id"}
                 ,{"name": "Course Name", "id": "course_name"}
                 ,{"name": "Course Lesson ID", "id": "course_lesson_id"}
                 ,{"name": "Course Lesson Name", "id": "course_lesson_name"}
                 ,{"name": "Number of Labs", "id": "number_of_labs"}
                 ,{"name": "Labs Attempted", "id": "labs_attempted"}
                 ,{"name": "Score", "id": "score"}],
        data=dataframe.to_dict('records'),
        #filter_action="native",
        #sort_action="native",
        style_table={"height": "200px", "overflowY": ""},
        style_cell={'textAlign': 'left'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
            }
        )

def all_users_scores():
    
    return dash_table.DataTable(
        id='all-users-table',
        columns=[{"name": "Username", "id": "username"}
                 ,{"name": "Total Labs", "id": "total_labs"}
                 ,{"name": "Total Labs Attempted", "id": "total_labs_attempted"}
                 ,{"name": "Total Score", "id": "total_score"}],
        data=queries.get_all_users().to_dict('records'),
        filter_action="native",
        sort_action="native",
        style_table={"height": "500px", "overflowY": "auto"},
        style_cell={'textAlign': 'left'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
            }
        ),