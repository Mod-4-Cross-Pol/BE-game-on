import requests
import unittest
import json
from app import app
import seed
from models import Event

class TestApp(unittest.TestCase):
    def setUp(self):
		    app.config.from_object('config.TestingConfig')
		    self.app = app.test_client()

        
    def test_root_page(self):
		    response = self.app.get('/')
		    self.assertEqual(200, response.status_code)


    def test_events_index_requests(self):
        headers = {'Content-Type': 'application/json'}
       
        response = self.app.get('/api/v1/events', headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        
        json_data = json.loads(response.data)

        self.assertEqual(json_data['data'][0]['activity'], 'Kickball')
        
        array_of_keys = list(json_data['data'][0].keys())
        
        self.assertEqual(len(array_of_keys), 13)
        self.assertEqual(array_of_keys.pop(0), 'activity')


    def test_events_patch_request(self):
        headers = {'Content-Type': 'application/json'}

        event = Event.query.first()
        event.id = 1
        event.current_participant_count = 5
        event.max_participant_count = 8   

        response = self.app.patch('/api/v1/events/1', headers=headers)

        self.assertEqual(response.status_code, 200)

        response = self.app.get('/api/v1/events', headers=headers)
        json_data = json.loads(response.data)

        self.assertEqual(json_data['data'][-1]['current_participant_count'], 6)
        self.assertEqual(json_data['data'][-1]['attending'], True)

    def test_patch_twice_toggles_attending_to_false(self):
        headers = {'Content-Type': 'application/json'}

        event = Event.query.first()
        event.id = 2
        event.current_participant_count = 5
        event.max_participant_count = 8 

        # first patch
        response = self.app.patch('/api/v1/events/2', headers=headers)
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/api/v1/events', headers=headers)
        json_data = json.loads(response.data)


        # increments participant count by 1
        self.assertEqual(json_data['data'][-1]['current_participant_count'], 6)

        # attending changes to true
        self.assertEqual(json_data['data'][-1]['attending'], True)
        
        # second patch
        response2 = self.app.patch('/api/v1/events/2', headers=headers)
        self.assertEqual(response2.status_code, 200)

        response2 = self.app.get('/api/v1/events', headers=headers)
        json_data2 = json.loads(response2.data)
        
        # participant leaves, so count decreases back to original
        self.assertEqual(json_data2['data'][-1]['current_participant_count'], 5)
        
        # attending toggles to false
        self.assertEqual(json_data2['data'][-1]['attending'], False)

    def test_post_events(self):
        headers = {'Content-Type': 'application/json'}

        response = self.app.post('/api/v1/events?date=2020-04-13&time=1230&duration=1:30&description=playing volleyball at wash park. need 4!&location=Wash Park&current_participant_count=6&max_participant_count=10&activity=volley ball&equipment=net, ball&skill_level=Beginner', headers=headers)
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/api/v1/events', headers=headers)
        json_data = json.loads(response.data)

        self.assertEqual(len(json_data['data']), 3)

    
    def test_delete_events(self):
        headers = {'Content-Type': 'application/json'}
 
        response = self.app.get('/api/v1/events', headers=headers)
        json_data = json.loads(response.data)
        
        self.assertEqual(len(json_data['data']), 3)

        response = self.app.delete('/api/v1/events/1', headers=headers)

        self.assertEqual(response.status_code, 200)

        response = self.app.get('/api/v1/events', headers=headers)
        json_data = json.loads(response.data)

        self.assertEqual(len(json_data['data']), 2)

# json_data = json.loads(response.data)
        # print(json_data)
        # event_list = list(json_data['data'])
        # print(event_list)
        # self.assertEqual(len(event_list), 1)

# params = {'date': '2020-04-13',
#           'time': '1230',
#           'duration': '1:30',
#           'description': 'playing volleyball at wash park. need 4!',
#           'location': 'Wash Park',
#           'current_participant_count': 6,
#           'max_participant_count': 10,
#           'activity': 'volley ball',
#           'equipment': 'net, ball',
#           'skill_level': 'Beginner'}
