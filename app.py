import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from models import *
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import geo_service
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)
load_dotenv()

parser = reqparse.RequestParser()

@app.route('/')
@app.route('/api/v1')
def home_page():
  return "Honey I'm home and I have an API"

@app.route('/api/v1/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
  id = event_id
  event = Event.query.filter_by(id=id)[0]
  db.session.delete(event)
  db.session.commit()
  return """
      <h1>Event Successfully Deleted!</h1>
    """

@app.route('/api/v1/events/<int:event_id>', methods=['PATCH'])
def add_participant(event_id):
  id = event_id
  event = Event.query.filter_by(id=id)[0]
  if event.current_participant_count < event.max_participant_count:
    event.current_participant_count += 1
    event.attending = True
    db.session.commit()
    return """
        <h1>Participant Successfully Added!</h1>
      """
  else:
    return """
        <h1>Max Participants Reached!</h1>
      """

class Events(Resource):
  def get(self):
    if request.args.get('date'):
      string_date = request.args.get('date')
      to_date = datetime.strptime(string_date, '%Y-%m-%d').date()
      events = Event.query.filter(Event.date==to_date)
    else:
      events = Event.query.all()
    event_schema = EventSchema(many=True)
    output = event_schema.dump(events)
    return jsonify({'data': output})

  def post(self):
    date = request.args.get('date')
    activity = request.args.get('activity')
    description = request.args.get('description')
    duration = request.args.get('duration')
    equipment = request.args.get('equipment')
    location = request.args.get('location')
    lat_long = geo_service.find_coordinates(location)
    max_participant_count = request.args.get('max_participant_count')
    current_participant_count = request.args.get('current_participant_count')
    start_time = request.args.get('start_time')
    skill_level = request.args.get('skill_level')
    attending = request.args.get('attending')

    new_event = Event(
                      date = date, 
                      start_time = start_time, 
                      duration = duration, 
                      description = description,
                      location = location, 
                      lat_long = lat_long,
                      current_participant_count = current_participant_count,
                      max_participant_count = max_participant_count,
                      activity = activity,
                      equipment = equipment,
                      skill_level = skill_level,
                      attending = attending
                    )

    db.session.add(new_event)
    db.session.commit()
    return """
      <h1>Event Successfully Created!</h1>
    """

api.add_resource(Events, '/api/v1/events')

@app.route('/api/v1/seed')
def seed():
  import seed
  return """
    <h1>Data Successfully Seeded!</h1>
  """

if __name__ == '__main__':
  app.run()
