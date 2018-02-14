import psycopg2
from sshtunnel import SSHTunnelForwarder

from secret.confidential import *

from app import logging

## PostgreSQL

# Create an SSH tunnel
tunnel = SSHTunnelForwarder(
    (IP_ADDR, 22),
    ssh_username=SSH_USERNAME,
    ssh_password=SSH_PASSWORD,
    remote_bind_address=('localhost', 5432)
)
# Start the tunnel
tunnel.start()

# Create a database connection
conn = psycopg2.connect(
    database=DATABASE,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=tunnel.local_bind_host,
    port=tunnel.local_bind_port,
)
conn.autocommit = True

logging.info("Connect to database successfully.")

# Get a database cursor
cur = conn.cursor()

def close_db():
    # Close connection to database
    global conn
    conn.close()

    # Stop the tunnel
    global tunnel
    tunnel.stop()
    logging.info("\nClosed connections successfully.")
