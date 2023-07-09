import time
import psycopg2
from psycopg2 import Error
from psycopg2 import extras
from dotenv import dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")


db = config["DB_NAME"]
user = config["DB_USER"]
password = config["DB_PASSWORD"]
host = config["DB_HOST"]
port = config["DB_PORT"]

while True:
    try:
        conn = psycopg2.connect(
            host=host, port=port, database=db, user=user, password=password
        )
        cursor = conn.cursor(cursor_factory=extras.DictCursor)
        print("Connection to Postgres successful")
        break
    except Exception as error:
        print("Error while connecting to PostgreSQL:", error)
        time.sleep(2)
