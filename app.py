import os
from flask import Flask, jsonify
from models import *
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import gardener

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
@app.route('/api/v1')
def home_page():
  return "Honey I'm home and I have an API"

@app.route('/api/v1/events', methods=['GET'])
def current_events():
  events = Event.query.all()
  event_schema = EventSchema(many=True)
  output = event_schema.dump(events)
  return jsonify({'data': output})


@app.route('/api/v1/events/create', methods=['POST'])
def create_events():
  
  
  # events = Event.query.all()
  # event_schema = EventSchema(many=True)
  # output = event_schema.dump(events)
  # return jsonify({'data': output})

@app.route('/api/v1/seed')
def seed():
  import gardener
  return """
    <h1>Data successfully seeded!</h1>
    <p>Visit -- api/v1/EVENTS -- to see updated information</p>
  """
  

if __name__ == '__main__':
  app.run()
