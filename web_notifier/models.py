import os
import datetime
from flask_mongoengine import MongoEngine

DB_URL = os.environ.get("DB_URL")

db = MongoEngine()

class Url(db.Document):
    title = db.StringField()
    url = db.StringField()
    modified_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title

class Item(db.Document):
    guid = db.StringField()
    title = db.StringField()
    description = db.StringField()
    modified_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title



