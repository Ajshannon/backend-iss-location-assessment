import requests
import urllib
# import urllib.request
import json
from datetime import datetime
import turtle
import time

api_url_base = 'http://api.open-notify.org/iss-now.json'
headers = {'Content-Type': 'application/json'}


def iss():
    api = api_url_base

    response = requests.get(api, headers=headers)

    if response.status_code == 200:
        scrape_iss(response, api)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api))
        return None


def scrape_iss(response, api):
    iss = json.loads(response.content.decode('utf-8'))
    iss_pos = iss['iss_position']
    lat = float(iss_pos['latitude'])
    lon = float(iss_pos['longitude'])
    timestamp = iss['timestamp']

    print datetime.utcfromtimestamp(
        timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print "Latitude: " + str(lat)
    print "Longitude: " + str(lon)
    iss_display(lon, lat, api)


def iss_display(lon, lat, api):

    screen = turtle.Screen()
    # Set screen size
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')

    # Iss Turtle
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)

    iss.penup()
    iss.goto(lon, lat)

    # Indianpolis Space Center

    indy_lat = 39.7684 + 2.25
    indy_lon = -86.1581 - 4.15

    # hou_lat = 29.5502
    # hou_lon = -95.097

    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(indy_lon, indy_lat)
    location.dot(5)

    api = 'http://api.open-notify.org/iss-pass.json?lat=' + \
        str(lat) + '&lon=' + str(lon)
    response = requests.get(api, headers=headers)
    iss = json.loads(response.content.decode('utf-8'))

    over = iss['response'][1]['risetime']
    location.write(time.ctime(over))

    turtle.mainloop()
