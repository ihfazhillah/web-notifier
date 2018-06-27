from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

from web_notifier.models import Url, Item

admin = Admin(name='Notifier Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Url))
admin.add_view(ModelView(Item))