from app import db
from sqlalchemy.dialects.postgresql import JSON

class Event(db.Model):
  __tablename__ = 'events'

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String())
  location = db.Column(db.String())
  start_time = db.Column(db.DateTime())
  end_time = db.Column(db.DateTime())
  current_participant_count = db.Column(db.Integer())
  max_participant_count = db.Column(db.Integer())
  activity = db.Column(db.String())

  def __init__(self, description, location, start_time, end_time, current_participant_count, max_participant_count, activity):
    self.description = description
    self.location = location
    self.start_time = start_time
    self.end_time = end_time
    self.current_participant_count = current_participant_count
    self.max_participant_count = max_participant_count
    self.activity = activity

  def __repr__(self):
    return '<id {}>'.format(self.id)
