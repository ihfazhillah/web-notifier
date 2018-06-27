import os

DB_URL = os.environ.get('DB_URL')

MONGODB_SETTINGS = {
   'db': 'upwork',
   'host': DB_URL
}