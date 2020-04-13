from models import *

db.drop_all()
db.create_all()

event1 = Event(
	date = '2020-11-05', 
	start_time = '1200', 
	duration = '3:00', 
	description = 'Hoopin at City Park', 
	location = 'City Park', 
	lat_long = '39.761,-105.012',
	current_participant_count = 6,
	max_participant_count = 10,
	activity = 'Basketball',
	equipment = 'nets, puck',
	skill_level = "Beginner"
)
db.session.add(event1)

event2 = Event(
	date = '2020-11-04', 
	start_time = '1400', 
	duration = '01:30', 
	description = 'Ball kicking at the Pepsi Center', 
	location = 'Pepsi Center', 
	lat_long = '39.748,-105.009',
	current_participant_count = 10,
	max_participant_count = 20,
	activity = 'Kickball',
	equipment = 'bases, ball',
	skill_level = "Expert"
)
db.session.add(event2)


event3 = Event(
	date = '2020-11-15', 
	start_time = '1500', 
	duration = '01:30', 
	description = 'Hotdog-eating competition', 
	location = 'Pepsi Center', 
	lat_long = '39.748,-105.009',
	current_participant_count = 25,
	max_participant_count = 35,
	activity = 'Miscellaneous',
	equipment = '',
	skill_level = "Beginner"
)
db.session.add(event3)

db.session.commit()