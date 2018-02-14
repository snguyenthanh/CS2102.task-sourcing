# Import the cursor from Postgres Client
from get_data.from_sql.postgres_client import cur

# This serves as a `void` function, where no data is returned
def sql(query):
    cur.execute(query)

# This function returns all rows as a list of tuples
# If no data is found, return an empty list
def sql_select(query):
    cur.execute(query)
    return cur.fetchall()
