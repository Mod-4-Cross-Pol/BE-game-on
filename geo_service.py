import os
import app
from flask import jsonify
from models import *
import googlemaps
from dotenv import load_dotenv
load_dotenv()


def find_coordinates(location):
   gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])
   lat_lng = gmaps.geocode(location)[0]['geometry']['location']
   return ("% s,% s"%(lat_lng['lat'], lat_lng['lng']))

