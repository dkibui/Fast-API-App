import psycopg2
from psycopg2 import Error

user = "postgres"
password = "3786"
host = "localhost"
db = "fastapi"
port = 5432


def db_connection():
    try:
        connection = psycopg2.connect(
            host=host, port=port, database=db, user=user, password=password
        )
        print("Connection to Postgres successful")
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
