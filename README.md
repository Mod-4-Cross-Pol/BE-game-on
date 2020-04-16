# GameOn Backend Api
```
Host:       Heroku 
Language:   Python
Framework:  Flask 
Database:   PostgreSQL
GameOnBE:   https://game-on-pro.herokuapp.com
```

### Overview
GameOn Backend is an API only app that allows users to interact with our database so they can easily create, read, update, and delete events. 

### Backend Repo
https://github.com/Mod-4-Cross-Pol/BE-game-on

### Frontend Repo
https://github.com/Mod-4-Cross-Pol/FE_game_on

### Front End Project Creators:
Zachary Nemeroff https://github.com/ZaneMeroff<br>
Ryan Novak https://github.com/ryan-novak

### Back End Project Creators:
Phil DeLong https://github.com/philjdelong<br>
Jordan Holtkamp https://github.com/jordanholtkamp

### Formatting
- Base URL for all endpoints: http://game-on-pro.herokuapp.com
- Each collection is returned within a hash that has a key of 'data' and a value of an array, containing objects returned in a hash format.
- Example:
_request_: GET http://game-on-pro.herokuapp.com/api/v1/events
_response body_: <br>
```
{ 
  "data": [
    {
      "activity": "Soccer",
      "attending": true,
      "current_participant_count": 2,
      "date": "2020-04-15",
      "description": "",
      "duration": "30 min",
      "equipment": "ball",
      "id": 49,
      "lat_long": "39.7365497,-104.9899995",
      "location": "Civic Center Park",
      "max_participant_count": 2,
      "skill_level": "Just for fun!",
      "start_time": "6:00AM" 
    }
  ]
}
```

### Getting Started
- To consume GameOnBE data, we will send requests to: https://game-on-pro.herokuapp.com/api/v1/events
- Instructions for CRUD endpoints include: [GET, POST, PATCH, DELETE]

### Endpoints
**Seed Events**
- _Method_: ["GET"]
- _URI_: '/api/v1/seed'
- _Seeds_: Three pre-created sample events.
- FOR TESTING AND DEVELOPMENT ONLY.

**Events Index**
- _Method_: ["GET"]
- _URI_: '/api/v1/events'
- _Returns_: All Events and attributes:
	- :id
	- :date
  - :activity
  - :description
  - :location
  - :lat_long
  - :start_time
  - :duration
  - :max_participant_count
  - :current_participant_count
  - :skill_level

**Events Index By Date**
- _Method_: ["GET"]
- _URI_: '/api/v1/events?date=YYYY-MM-DD'
- _Returns_: All Events and attributes associated with the date entered. Date specified in query params.

**Events New**
- _Method_: ["POST"]
- _URI_: '/api/v1/events'
- _Creates_: New event and assigns all default attributes.
- _Additional Info_: All attributes and information must be entered into the params, saparated by '&'
- All attributes are optional, EXCEPT **'location'**, Google API will return a 400 response and the instance will not be saved.
- _Example_:
POST '/api/v1/events?date=2020-04-13&time=1230&duration=1:30&description=playing volleyball at wash park, need 4!&location=Wash Park&current_participant_count=6&max_participant_count=10&activity=volley ball'

**Events Update**
- _Method_: ["PATCH"]
- _URI_: '/api/v1/events/:id'
- _Updates_: Updates Event with corresponding :id. This will not update Event information. Visiting this endpoint will increment or decrement 'current_participant_count' based on the 'attending' value.
- _Example_: 
if event.attending == True => return {event.attending = False, current_participant_count -= 1}
  
**Events Delete**
- _Method_: ["DELETE"]
- _URI_: '/api/v1/events/:id'
- _Deletes_: Deletes Event instance with corresponding :id
