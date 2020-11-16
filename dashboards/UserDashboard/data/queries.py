import yaml
import psycopg2
with open("cred_refactored.yaml") as cred_refactored: 
    refactored_creds = yaml.safe_load(cred_refactored)

import yaml
import psycopg2
with open("cred_rfanalytics.yaml") as cred_rfanalytics: 
    rfanalytics_creds = yaml.safe_load(cred_rfanalytics)

import sqlalchemy as sa
import pandas as pd 

host1 = refactored_creds['host']
username1 = refactored_creds['user']
password1 = refactored_creds['passwd']
port1 = refactored_creds['port']
database1 = refactored_creds['dbname']
engine_refactored = sa.create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(username1, password1,host1,port1, database1))
metadata_refactored = sa.MetaData(engine_refactored)
connection_refactored = engine_refactored.connect()


host2 = rfanalytics_creds['host']
username2 = rfanalytics_creds['user']
password2 = rfanalytics_creds['passwd']
port2 = rfanalytics_creds['port']
database2 = rfanalytics_creds['dbname']
engine_rfanalytics = sa.create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(username2, password2,host2,port2, database2))
metadata_rfanalytics = sa.MetaData(engine_rfanalytics)
connection_rfanalytics = engine_rfanalytics.connect()
    
def new_users_by_week():    
    return pd.read_sql(
        "SELECT date(date_trunc('week',date_joined)) as week,count(distinct id) as users FROM common_user group by date(date_trunc('week',date_joined))",
        con=engine_refactored)

def new_users_by_week_list(input_date): 
    #input_date = '2020-09-28'
    return pd.read_sql(
        "SELECT distinct email,first_name,last_name,username,date(date_joined) as date_joined,date(last_login) as last_login FROM common_user where date(date_trunc('week',date_joined)) ='%s'"%input_date,
        con=engine_refactored)

def users_by_day():
    return pd.read_sql(
        "SELECT date(hit_on) as date,count(distinct user_id) as users FROM common_usersession GROUP BY date(hit_on)",
        con=engine_refactored)

def users_by_day_list(input_date): 
    #input_date = '2020-09-28'
    return pd.read_sql(
        "SELECT distinct email,first_name,last_name,username,date(date_joined) as date_joined,date(last_login) as last_login FROM common_user where id in (select distinct user_id from common_usersession where date(hit_on)='%s')"%input_date,
        con=engine_refactored)

def users_visiting_notebooks_by_day():
    return pd.read_sql(
        "SELECT date(last_visit) as date,count(distinct username) as users FROM common_notebookvisit GROUP BY date(last_visit)",
        con=engine_rfanalytics)

# def users_visiting_notebooks_by_day_list(input_date): 
#     #input_date = '2020-09-28'
#     return pd.read_sql(
#         "SELECT distinct email,first_name,last_name,username,date(date_joined) as date_joined,date(last_login) as last_login FROM common_user where date(last_login)='%s'"%input_date,
#         con=engine_refactored)

def user_activity_per_hour():
    return pd.read_sql(
        "SELECT date_trunc('hour',created_at) as hour,count(url) as url FROM common_urlvisit GROUP BY date_trunc('hour',created_at) order by 1 asc",
        con=engine_rfanalytics)


