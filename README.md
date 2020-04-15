# GameOn Backend Api
Host:       Heroku 
Language:   Python
Framework:  Flask 
Database:   SQLAlchemy
**GameOnBE: 'https://game-on-pro.herokuapp.com'**

### Formatting
- The GameOnBE App follows REST API convention, displaying data in JavaScript Object Notation(JSON).
- Each collection is returned within a 'data:' hash
- Example:
_request_: GET 'http://game-on-pro.herokuapp.com/api/v1/events'
_response body_:
{
    "data": [
        {
            "activity": "String",
            "attending": true,
            "current_participant_count": 2,
            "date": "2020-04-15",
            "description": "",
            "duration": "30 min",
            "equipment": "ball,  attitude",
            "id": 49,
            "lat_long": "39.7365497,-104.9899995",
            "location": "Civic Center Park",
            "max_participant_count": 2,
            "skill_level": "Just for fun!",
            "start_time": "6:00AM"
        }
    ]
}

### Getting Started
- To consume GameOnBE data, we will send requests to: 'https://game-on-pro.herokuapp.com/api/v1/events'
- Instructions for CRUD endpoints include: [GET, POST, PATCH, DELETE]

### Endpoints
**Seed Events**
- __Method__: ["GET"]
- __URI__: '/api/v1/seed'
- __Seeds__: Three pre-created sample events.
- FOR TESTING AND DEVELOPMENT ONLY.

**Events Index**
- __Method__: ["GET"]
- __URI__: '/api/v1/events'
- __Returns__: Lists all Events and attributes:
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

**Events New**
- __Method__: ["POST"]
- __URI__: '/api/v1/events'
- __Creates__: New event and assigns all default attributes.
- All attributes and information must be entered into the params, saparated by '&'
- All attributes are optional, EXCEPT **'location'**, Google API will return a 400 response and the instance will not be saved.
- Example:
POST '/api/v1/events?date=2020-04-13&time=1230&duration=1:30&description=playing volleyball at wash park, need 4!&location=Wash Park&current_participant_count=6&max_participant_count=10&activity=volley ball'

**Events Update**
- __Method__: ["PATCH"]
- __URI__: '/api/v1/events/:id'
- __Updates__: Updates Event with corresponding :id. This will not update Event information. Visiting this endpoint will increment or decrement 'current_participant_count' based on the 'attending' value.
- Example: 
if event.attending == True => return {event.attending = False, current_participant_count -= 1}
  
**Events Delete**
- __Method__: ["DELETE"]
- __URI__: '/api/v1/events/:id'
- __Deletes__: Deletes Event instance with corresponding :id