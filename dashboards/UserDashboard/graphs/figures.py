import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd 
import plotly.express as px
from data import(
    queries,
    )

def new_users_by_week_bar_graph():
    new_users_by_week = queries.new_users_by_week()
    return px.bar(new_users_by_week, x="week", y="users",labels={
                     "week": "Week",
                     "users": "New Users",
                 },
                 #title="New Users Per Week",
                )

def users_by_day_bar_graph():
    users_by_day = queries.users_by_day()
    return px.bar(users_by_day, x="date", y="users",labels={
                          "date": "Day",
                          "users": "Number of Users",
                      },
                      #title="Number of Users Per day"
                      )

def users_visiting_notebooks_line_graph():
    users_visiting_notebooks_by_day = queries.users_visiting_notebooks_by_day()
    return px.line(users_visiting_notebooks_by_day, x="date", y="users",labels={
                      "date": "Day",
                      "users": "Number of Unique Users Per Day",
                  },
                  #title="Unique Users Visiting Notebooks"
                  )


def user_activity_per_hour():
    user_activity_per_hour = queries.user_activity_per_hour()
    return px.line(user_activity_per_hour, x="hour", y="url",labels={
                      "hour": "Time",
                      "url": "Number of URL hits",
                  },
                  #title="User Activity per Hour"
                  )

def generate_users_by_week_table(input_date):
    dataframe = queries.new_users_by_week_list(input_date)
    dataframe.rename(columns={"username": "Username", "first_name": "First Name", "last_name": "Last Name", "date_joined": "Date Joined", "last_login": "Last Login"})
    return dash_table.DataTable(
        id='table',
        columns=[{"name": "Email", "id": "email"}
                 ,{"name": "First Name", "id": "first_name"}
                 ,{"name": "last Name", "id": "last_name"}
                 ,{"name": "Username", "id": "Username"}
                 ,{"name": "Date Joined", "id": "date_joined"}
                 ,{"name": "last Login", "id": "last_login"}],
        data=dataframe.to_dict('records'),
        filter_action="native",
        sort_action="native",
        style_table={"height": "200px", "overflowY": "auto"},
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

def generate_users_by_day_table(input_date):
    dataframe = queries.users_by_day_list(input_date)
    dataframe.rename(columns={"username": "Username", "first_name": "First Name", "last_name": "Last Name", "date_joined": "Date Joined", "last_login": "Last Login"})
    return dash_table.DataTable(
        id='table',
        columns=[{"name": "Email", "id": "email"}
                 ,{"name": "First Name", "id": "first_name"}
                 ,{"name": "last Name", "id": "last_name"}
                 ,{"name": "Username", "id": "Username"}
                 ,{"name": "Date Joined", "id": "date_joined"}
                 ,{"name": "last Login", "id": "last_login"}],
        data=dataframe.to_dict('records'),
        filter_action="native",
        sort_action="native",
        style_table={"height": "200px", "overflowY": "auto"},
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

def generate_unique_users_visiting_notebooks_by_day_table(input_date):
    dataframe = queries.users_visiting_notebooks_by_day_list(input_date)
    dataframe.rename(columns={"username": "Username", "first_name": "First Name", "last_name": "Last Name", "date_joined": "Date Joined", "last_login": "Last Login"})
    return dash_table.DataTable(
        id='table',
        columns=[{"name": "Email", "id": "email"}
                 ,{"name": "First Name", "id": "first_name"}
                 ,{"name": "last Name", "id": "last_name"}
                 ,{"name": "Username", "id": "Username"}
                 ,{"name": "Date Joined", "id": "date_joined"}
                 ,{"name": "last Login", "id": "last_login"}],
        data=dataframe.to_dict('records'),
        filter_action="native",
        sort_action="native",
        style_table={"height": "200px", "overflowY": "auto"},
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
    # max_rows = len(dataframe)
    # return html.Table([
    #     html.Thead(
    #         html.Tr([html.Th(col) for col in dataframe.columns])
    #     ),
    #     html.Tbody([
    #         html.Tr([
    #             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
    #         ]) for i in range(min(len(dataframe), max_rows))
    #     ])
    # ])