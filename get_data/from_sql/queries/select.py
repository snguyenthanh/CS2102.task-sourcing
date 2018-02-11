from get_data.from_sql.queries.select_queries import *
from get_data.from_sql.sql_executor import sql_select

def get_person(username):
    return sql_select(SELECT_ONE_USER_QUERY.format(username))

def get_email(email):
    return sql_select(SELECT_ONE_EMAIL_QUERY.format(email))

def get_person_with_pwd(username, password):
    return sql_select(SELECT_PERSON_WITH_PWD_QUERY.format(username, password))
