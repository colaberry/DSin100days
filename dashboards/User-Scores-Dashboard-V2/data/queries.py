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

def get_user_course_completion(user_name,course_name):
    query = """
         with t1 as /*form a table with users ,courses and number of sections in each course (course lessons)*/
        (
            select u.id as user_id
                ,u.username
                ,u.first_name
                ,u.last_name
                ,cd.course_id
                ,cd.course_name
                ,cd.total_sections::numeric,2
            from common_user u,
            (
                select c.id as course_id
                     ,c.title as course_name
                     ,count(distinct cl.id) as total_sections
                from common_courselesson cl inner join common_course c on cl.course_id = c.id 
                group by c.id,c.title
            ) as cd
            where u.username = %(var1)s and cd.course_name = %(var2)s
        )
        
        ,t2 as /*form a table as user,course and number of sections started/visited in that course*/
        (
            select ucl.user_id
                ,cl.course_id
                ,count(distinct ucl.course_lesson_id) as sections_visited
            from common_courselesson cl inner join common_usercourselesson ucl on cl.id = ucl.course_lesson_id
            group by ucl.user_id,cl.course_id
        )
        select t1.user_id
            ,t1.username
            ,t1.first_name
            ,t1.last_name
            ,t1.course_id
            ,t1.course_name
            ,100*round(coalesce((t2.sections_visited/t1.total_sections),0)::numeric,2) as percent_completed
        from t1 left join t2 on t1.user_id = t2.user_id and t1.course_id = t2.course_id 
             """ 
    return pd.read_sql_query(query, con=engine_refactored, params={"var1":user_name,"var2":course_name})
    
    
def get_user_course_details(user_name,course_name):
    
    query = """
        with t1 as /*form a table with users ,courses and course lessons*/
        (
            select u.id as user_id
                ,u.username
                ,cd.course_id
                ,cd.course_name
                ,cd.course_lesson_id
                ,cd.course_lesson_name
            from common_user u,
            (
                select c.id as course_id
                     ,c.title as course_name
                     ,cl.id as course_lesson_id
                     ,cl.title as course_lesson_name
                from common_courselesson cl inner join common_course c on cl.course_id = c.id 
            ) as cd
            where u.username = %(var1)s and cd.course_name = %(var2)s
        )
                
        , t2 as /*form a table with users ,courses and number of sections in each course (course lessons)*/
        (
            select t1.course_lesson_id
                ,t1.course_lesson_name
                ,coalesce(ucl.introduction_completed,False) as introduction_completed
                ,coalesce(ucl.notebook_completed,False) as notebook_completed
                ,coalesce(ucl.video_lab_completed,False) as video_lab_completed
                ,coalesce(ucl.lab_completed,False) as lab_completed
                ,coalesce(ucl.lab_score,0) as lab_score
                ,coalesce(ucl.quiz_completed,False) as quiz_completed
            from t1 left join common_usercourselesson ucl on t1.user_id = ucl.user_id and t1.course_lesson_id = ucl.course_lesson_id
        )
        select * from t2
            """ 
    
    data = pd.read_sql_query(query, con=engine_refactored, params={"var1":user_name,"var2":course_name})
    return data

def get_courses():
    query = """
        Select distinct title as course_name from common_course
        """
        
    df = pd.read_sql_query(query, con=engine_refactored)
    options = []
    for index,row in df.iterrows():
         options.append({'label':row[0], 'value':row[0]})
    return options