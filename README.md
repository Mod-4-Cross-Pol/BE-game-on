# GameOn Backend Api
The Backend app for GameOn is hosted on Heroku, written in Python, using the Flask framework with data accessed through MongoDB.
__GameOnBE: 'https://game-on-cross-pol.herokuapp.com/api/v1'__

### Formatting
The GameOnBE App follows REST API convention, displaying data in JavaScript Object Notation(JSON).

### Getting Started
We currently have data available for activities (index, show), 10 instances pre-populated within our Database (MongoDB). 

### Future Additions
- Events (Index, Show, Create, Destroy)
- Feature: Activities can be added when creating New Events.

### Endpoints
__Activities Index__
- Method: ["GET"]
- URI: '/activities'
- Display: Lists all activities and attributes:
	- :name
	- :description
	- :id
  
__Activities Show__
- Method: ["GET"]
- URI: '/activities/:id'
- Display: Activity info for corresponding :id