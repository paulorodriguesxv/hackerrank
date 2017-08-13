#encoding: utf8
"""
Submissions
Leaderboard
Discussions
Destinations often have lots of attractions or landmarks that travelers want to visit – usually more than they can visit during their stay. What most travelers end up doing is optimizing their time by only visiting the attractions that are closest to where they’re staying.

Travelers ask you to help them to arrange holiday, so they can visit as many attractions as possible. Your task is to calculate the time it takes from the hotel to the attractions by preferred transport for the given amount of time. Transport can be only be one of the followings: foot, bike or metro.

Notes:

You should consider the following average speed for the different transport options: metro, 20km/h; bike, 15km/h; and foot, 5km/h
For distances in the problem you should use the 'Law of Cosines for Spherical Trigonometry'. Here how it is implemented as pseudo-code.
function distance_between(point1, point2) {
    var EARTH_RADIUS = 6371;//in km
    var point1_lat_in_radians  = degree2radians( point1.latitude );
    var point2_lat_in_radians  = degree2radians( point2.latitude );
    var point1_long_in_radians  = degree2radians( point1.longitude );
    var point2_long_in_radians  = degree2radians( point2.longitude );

    return acos( sin( point1_lat_in_radians ) * sin( point2_lat_in_radians ) +
                 cos( point1_lat_in_radians ) * cos( point2_lat_in_radians ) *
                 cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS;
}
    
When calculating distance, always round it up or down to 2 decimal points precision. Example: 2.3467 should be rounded to 2.35 while 3.4522 should be rounded to 3.45
All values of integer type should be considered as 4-bytes integer.
Assume value of pi is 3.14159265359.
Input Format

The first line contains an integer , which represents the number of attractions that follows. After that are  lines each containing three space-separated numbers that represent the ID (integer), the latitude (double) and the longitude (double) of the attraction.

After the attractions there will be another line containing an integer , which represents the number of test cases that follows. After that are  lines each containing four space-separated values – the first and second are the latitude (double) and longitude (double) of the hotel the guest is staying at, the third value shows their preferred transport option and the fourth represents how long they are willing to travel in minutes starting from the hotel.

Output Format

The output is precisely  lines, each containing a list of space-separated attraction IDs. Each line represents the attractions that are possible to reach from the guest’s hotel in the specified amount of time and using the preferred transport option. In each line the attraction IDs should be sorted by distance starting with the closest one. When two attractions are the same distance away, they should be sorted by ID.

 is no greater than 200.  is no greater than 200.

Sample Input

10
1 52.378281 4.900070
2 52.373634 4.890289
3 52.375737 4.896547
4 52.372995 4.893096
5 52.376237 4.902860
6 52.367066 4.893381
7 52.366537 4.911348
14 52.368832 4.892744
15 52.357895 4.892835
35 52.342497 4.855094
5
52.379141 4.880590 metro 80
52.358835 4.893867 foot 60
52.375859 4.886006 foot 30
52.371700 4.899070 metro 30
52.364055 4.898446 foot 60
Sample Output

2 4 3 1 14 5 6 15 7 35
15 6 14 7 4 2 3 5 1 35
2 4 3 14 1 6 5 7 15
4 3 14 5 2 6 1 7 15 35
6 14 15 7 4 2 3 5 1 35 
"""

from __future__ import division
import operator
from math import radians, sin, cos, acos


METROSPEED = 20
BIKESPEED = 15
FOOTSPEED = 5

class Coord(object):

    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

class EntityCoord(object):

    def getCoord(self):
        pass

class Attraction(EntityCoord):

    def __init__(self, stream):

        streamlist = stream.split()

        self.aid = streamlist[0]
        self.coord = Coord(streamlist[1], streamlist[2])

    def getCoord(self):
        return self.coord

class User(EntityCoord):

    def __init__(self, stream):
        streamlist = stream.split()

        self.Hotel = Coord(streamlist[0], streamlist[1])
        self.transport = self.transpCorrelation(streamlist[2])
        self.totalTime = float(streamlist[3]) / 60

    def transpCorrelation(self, transport):
        tra = dict(metro=METROSPEED, bike=BIKESPEED, foot=FOOTSPEED)

        return tra[transport]


    def getCoord(self):
        return self.Hotel


def populate_attractions(filehandle):

    qtdeAttractions = int(filehandle.readline())

    attractions = [Attraction(filehandle.readline()) for line in xrange(qtdeAttractions)]

    return attractions

def populate_userdata(filehandle):

    qtdeHotels = int(filehandle.readline())

    hotels = [User(filehandle.readline()) for line in xrange(qtdeHotels)]

    return hotels



def distance_between(point1, point2, transport):
    EARTH_RADIUS = 6371; # in km
    point1_lat_in_radians  = radians(point1.latitude)
    point2_lat_in_radians  = radians(point2.latitude)
    point1_long_in_radians  = radians(point1.longitude)
    point2_long_in_radians  = radians(point2.longitude)

    dist = round(acos( sin( point1_lat_in_radians ) * sin( point2_lat_in_radians ) + 
                 cos( point1_lat_in_radians ) * cos( point2_lat_in_radians ) *
    cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS, 2)

    time = dist / transport

    return dict(distance=dist, timespent=time) 

def byDistance(comp1, comp2):

    if comp1[1]["timespent"] < comp2[1]["timespent"]:
        return -1
    elif comp1[1]["timespent"] == comp2[1]["timespent"]:

        if int(comp1[0]) < int(comp2[0]):
            return -1
        else:
            return 1
    else:
        return 0
    #return data[1]["timespent"]

filehandle = open('nearby-attractions.txt', 'r')

attractions = populate_attractions(filehandle)
users = populate_userdata(filehandle)


for user in users:
    pickedList = ''
    distances = {x.aid:distance_between(user.getCoord(), x.getCoord(), user.transport) for x in attractions}

    distances = sorted(distances.items(), cmp=byDistance)

    soma = 0
    for distance in distances:

        soma += distance[1]["timespent"]

        if distance[1]["timespent"] <= user.totalTime:
            pickedList += distance[0] + ' '

    print pickedList
