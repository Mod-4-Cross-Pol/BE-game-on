from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import *
import os


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# ma = Marshmallow(app)

# class EventSchema(ma.ModelSchema):
#   class Meta:
#     model = Event
# print(db.events)

@app.route('/')
@app.route('/api/v1')
def home_page():
  return "Honey I'm home and I have an API"

@app.route('/api/v1/events')
def current_events(methods=['GET', 'POST']):
  events = Event.query.all()
  event_schema = EventSchema(many=True)
  output = event_schema.dump(events)
  return jsonify({'data': output})



if __name__ == '__main__':
  app.run()
