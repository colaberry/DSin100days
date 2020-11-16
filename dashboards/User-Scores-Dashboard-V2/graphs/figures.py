import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd 
import plotly.express as px
from data import(
    queries,
    )

def user_completion_table(input_username,input_coursename):
    dataframe = queries.get_user_course_completion(input_username,input_coursename)
    return dash_table.DataTable(
        id='user-completion-table',
        columns=[{"name": "User ID", "id": "user_id"}
                 ,{"name": "Username", "id": "username"}
                 ,{"name": "First Name", "id": "first_name"}
                 ,{"name": "Last Name", "id": "last_name"}
                 ,{"name": "Course ID", "id": "course_id"}
                 ,{"name": "Course Name", "id": "course_name"}
                 ,{"name": "Percent Complete", "id": "percent_completed"}],
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

def course_details_table(input_username,input_coursename):
    
    return dash_table.DataTable(
        id='course-details-table',
        columns=[{"name": "Course Lesson ID", "id": "course_lesson_id"}
                 ,{"name": "Course Lesson Name", "id": "course_lesson_name"}
                 ,{"name": "Introdcution Completed", "id": "introduction_completed"}
                 ,{"name": "Notebook Completed", "id": "notebook_completed"}
                 ,{"name": "Video Lab Completed", "id": "video_lab_completed"}
                 ,{"name": "Lab Completed", "id": "lab_completed"}
                 ,{"name": "Lab Score", "id": "lab_score"}
                 ,{"name": "Quiz Completed", "id": "quiz_completed"}],
        data=queries.get_user_course_details(input_username,input_coursename).to_dict('records'),
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