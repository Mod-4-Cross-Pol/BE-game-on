import os
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from models import *
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# import gardener

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument('params')


# @app.route('/')
# @app.route('/api/v1')
# def home_page():
#   return "Honey I'm home and I have an API"

class Events(Resource):
  def get(self):
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
    # lat_long = GoogleService.new.get_coords(request.args.get('location'))
    max_participant_count = request.args.get('max_participant_count')
    current_participant_count = request.args.get('current_participant_count')
    start_time = request.args.get('start_time')

    new_event = Event(
                      date = date, 
                      start_time = start_time, 
                      duration = duration, 
                      description = description,
                      location = location, 
                      lat_long = '39.761,-105.012',
                      current_participant_count = current_participant_count,
                      max_participant_count = max_participant_count,
                      activity = activity,
                      equipment = equipment
                    )

    db.session.add(new_event)
    db.session.commit()

    


api.add_resource(Events, '/api/v1/events')




# @app.route('/api/v1/events', methods=['GET'])
# def current_events():
#   events = Event.query.all()
#   event_schema = EventSchema(many=True)
#   output = event_schema.dump(events)
#   return jsonify({'data': output})


# @app.route('/api/v1/events/create', methods=['POST'])
# def create_events():
  
  
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
