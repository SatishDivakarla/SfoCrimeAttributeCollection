__author__ = 'SatishDivakarla'

import urllib, json

#Grabbing and parsing the JSON data
def GooglePlace(latitude,longitude,radius,types,key):
  #making the url
  AUTH_KEY = key
  LOCATION = str(latitude) + "," + str(longitude)
  RADIUS = radius
  TYPES = types
  MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)

  #grabbing the JSON result
  response = urllib.urlopen(MyUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  return jsonData


#This is a helper to grab the Json data that I want in a list
def IterJson(place):
  x = [place['name'], place['reference'], place['geometry']['location']['lat'],
         place['geometry']['location']['lng'], place['vicinity']]
  print x
  return x