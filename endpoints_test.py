import requests
import unittest
import json
from app import app

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
        self.assertEqual(json_data['data'][0]['activity'], 'spike ball')
        
        array_of_keys = list(json_data['data'][0].keys())
        
        self.assertEqual(len(array_of_keys), 11)
        self.assertEqual(array_of_keys.pop(0), 'activity')
        # self.assertEqual(response.json(), 'data')
        # print(response.json())
        
    def test_post_events(self):
        headers = {'Content-Type': 'application/json'}
        
        params = {'date': '2020-04-13', 'time': '1230', 'duration': '1:30', 'description': 'playing volleyball at wash park. need 4!', 'location': 'Wash Park', 'lat_long': '39.631,-104.973',  'current_participant_count': 6, 'max_participant_count': 10, 'activity': 'volley ball', 'equipment': 'net, ball'}

        response = self.app.post('/api/v1/events/create', data=params, headers=headers)
        self.assertEqual(response.status_code, 200)

# class TestApp(unittest.TestCase):
# 	def setUp(self):
# 		app.config.from_object('config.TestingConfig')
# 		self.app = app.test_client()
# 	def test_root_page(self):
# 		response = self.app.get('/')
# 		self.assertEqual(200, response.status_code)
# 	def test_search_endpoint(self):
# 		response = self.app.get('/search?type=author&q=george rr martin')
# 		self.assertEqual(200, response.status_code)
# 		json_data = json.loads(response.data)
# 		self.assertEqual(40, len(json_data.get('data')))