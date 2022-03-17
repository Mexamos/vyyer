import os

MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'root')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'db_name')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.getenv('MYSQL_PORT', 3306)

DB_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
