import os

MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'marcelino')
MYSQL_DB = os.getenv('MYSQL_DB', 'med_recordatorio')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')