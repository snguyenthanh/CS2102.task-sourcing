from get_data.from_sql.queries.insert_queries import *
from get_data.from_sql.sql_executor import sql

from time import gmtime, strftime
from secret.hash import encoded

from constraints.task import ALLOWED_STATUSES
from constraints.category import CATEGORIES

def insert_new_person(username, password, email):
    password = encoded(password)

    # Get current server time
    created_dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    sql(INSERT_PERSON_QUERY.format(username, password, email, created_dt))

def insert_all_statuses():
    for status in ALLOWED_STATUSES:
        sql(INSERT_TASK_STATUS_QUERY.format(status))

def insert_all_categories():
    for category in CATEGORIES:
        sql(INSERT_CATEGORY_QUERY.format(category))
