from get_data.from_sql.queries.create_queries import *
from get_data.from_sql.sql_executor import sql

def create_table_person():
    sql(CREATE_TABLE_PERSON_QUERY)

def create_table_category():
    sql(CREATE_TABLE_CATEGORY_QUERY)

def create_table_task():
    sql(CREATE_TABLE_TASK_QUERY)

def create_table_offer():
    sql(CREATE_TABLE_OFFER_QUERY)

def create_all_tables():
    create_table_person()
    create_table_category()
    create_table_task()
    create_table_offer()
