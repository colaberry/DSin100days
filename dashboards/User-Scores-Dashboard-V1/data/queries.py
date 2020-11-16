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

def get_all_users():
    query = """
         /*first get each user with number of labs for each course and course_lesson*/
          with t1 as 
         (
             Select u.id,u.username,l.course_id,c.title as course_name,cl.title as course_lesson_name,l.course_lesson_id,count(distinct l.id) as number_of_labs
             from common_user u,common_lab l,common_course c,common_courselesson cl
             where l.course_id = c.id and l.course_lesson_id = cl.id 
                 and l.course_id is not null 
             group by u.id,u.username,l.course_id,c.title,cl.title,l.course_lesson_id
         )
         
         /*next get each user and number of labs completed for a course and course_lesson*/
         ,t2 as 
         (
             Select u.id,u.username,l.course_id,l.course_lesson_id,count(distinct ulab.lab_id) as labs_attempted,sum(ulab.score) as score
             from common_user as u left join common_userlab as ulab on u.id = ulab.user_id 
                 right join common_lab as l on ulab.lab_id = l.id  
             group by u.id,u.username,l.course_id,l.course_lesson_id
         )
         
        /*join the tables to get details as - total number of labs, labs attempted, score for a given course and course_lesson*/
         ,t3 as 
         (
             select 
             t1.id
             ,t1.username
             ,t1.course_id
             ,t1.course_name
             ,t1.course_lesson_id
             ,t1.course_lesson_name
             ,t1.number_of_labs
             ,coalesce(t2.labs_attempted,0) as labs_attempted 
             ,coalesce(t2.score,0) as score 
         from t1 left join t2 on t2.id = t1.id and t2.course_id = t1.course_id 
             and t2.course_lesson_id = t1.course_lesson_id
        )
        
        select t3.username,sum(number_of_labs) as total_labs,sum(labs_attempted) as total_labs_attempted,sum(score) as total_score
        from t3
        group by t3.username
        order by 3 desc
             """ 
    return pd.read_sql_query(query, con=engine_refactored)
    
    
def get_user_score(user_name):
    
    query = """
            /*first get each user with number of labs for each course and course_lesson*/
             with t1 as 
            (
                Select u.id,u.username,u.first_name,u.last_name,u.email,l.course_id,c.title as course_name,cl.title as course_lesson_name,l.course_lesson_id,count(distinct l.id) as number_of_labs
                from common_user u,common_lab l,common_course c,common_courselesson cl
                 where l.course_id = c.id and l.course_lesson_id = cl.id 
                    and l.course_id is not null and u.username = %(var1)s 
                 group by u.id,u.username,l.course_id,c.title,cl.title,l.course_lesson_id
            )
            
            /*next get each user and number of labs completed for a course and course_lesson*/
            ,t2 as 
            (
                Select u.id,u.username,l.course_id,l.course_lesson_id,count(distinct ulab.lab_id) as labs_attempted,sum(ulab.score) as score
                from common_user as u left join common_userlab as ulab on u.id = ulab.user_id 
                    right join common_lab as l on ulab.lab_id = l.id  
                where u.username = %(var2)s
                group by u.id,u.username,l.course_id,l.course_lesson_id
            )
            
           /*join the tables to get details as - total number of labs, labs attempted, score for a given course and course_lesson*/
            select 
                t1.id
                ,t1.username
                ,t1.first_name
                ,t1.last_name
                ,t1.email
                ,t1.course_id
                ,t1.course_name
                ,t1.course_lesson_id
                ,t1.course_lesson_name
                ,t1.number_of_labs
                ,coalesce(t2.labs_attempted,0) as labs_attempted 
                ,coalesce(t2.score,0) as score 
            from t1 left join t2 on t2.id = t1.id and t2.course_id = t1.course_id and t2.course_lesson_id = t1.course_lesson_id""" 
    
    data = pd.read_sql_query(query, con=engine_refactored, params={"var1":user_name,"var2":user_name})
    return data

