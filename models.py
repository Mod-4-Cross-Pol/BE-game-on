from sqlalchemy.dialects.postgresql import JSON
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

ma = Marshmallow(app)
db = SQLAlchemy(app)
db.init_app(app)

app.config.from_object("config.ProductionConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Event(db.Model):
  __tablename__ = 'events'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date())
  start_time = db.Column(db.String())
  duration = db.Column(db.String())
  description = db.Column(db.String())
  location = db.Column(db.String())
  lat_long = db.Column(db.String())
  current_participant_count = db.Column(db.Integer())
  max_participant_count = db.Column(db.Integer())
  activity = db.Column(db.String())
  equipment = db.Column(db.String())

  def __init__(self, date, start_time, duration, description, location, lat_long, current_participant_count, max_participant_count, activity, equipment):
    self.date = date
    self.start_time = start_time
    self.duration = duration
    self.description = description
    self.location = location
    self.lat_long = lat_long
    self.current_participant_count = current_participant_count
    self.max_participant_count = max_participant_count
    self.activity = activity
    self.equipment = equipment

  def __repr__(self):
    return '<id {}>'.format(self.id)

class EventSchema(ma.ModelSchema):
  class Meta:
    model = Event