from get_data.from_sql.queries.insert_queries import *
from get_data.from_sql.sql_executor import sql

from time import gmtime, strftime
from secret.hash import encoded

def insert_new_person(username, password, email):
    password = encoded(password)
    
    # Get current server time
    created_dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    sql(INSERT_PERSON_QUERY.format(username, password, email, created_dt))
