# GameOn Backend Api
The Backend app for GameOn is hosted on Heroku, written in Python, using the Flask framework with data accessed through MongoDB.
__GameOnBE: 'https://game-on-pro.herokuapp.com'__

### Formatting
The GameOnBE App follows REST API convention, displaying data in JavaScript Object Notation(JSON).

### Getting Started
We currently have data available for activities (index, show), 10 instances pre-populated within our Database (MongoDB). 

### Future Additions
- Events (Index, Show, Create, Destroy)
- Feature: Activities can be added when creating New Events.

### Endpoints
__Events Index__
- Method: ["GET"]
- URI: '/api/v1/events'
- Display: Lists all Events and attributes:
	- :id
	- :date
  - :activity
	- :description
  - :location
  - :start_time
  - :duration
  - :max_participant_count
  - :current_participant_count
  - :lat_long (in process)

__Create Event__
- Method: ["POST"]
- URI: '/api/v1/events'
- Creates new event with given params

__Create Seeds__
- Method: ["GET"]
- URI: '/api/v1/seed'
- Destroys all events in DB and seeds events in seed file (3 right now)
  
__Activities Show__
- Method: ["GET"]
- URI: '/activities/:id'
- Display: Activity info for corresponding :id