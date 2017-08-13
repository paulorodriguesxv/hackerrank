

f = open('travel-profiles.txt', 'r')

from collections import Counter

class Budgets(object):

    def __init__(self, stream):
        liststream = stream.split()
        self.price = float(liststream[0])
        self.facilities = liststream[1:]


class Hotel(object):
    
    def __init__(self, stream):
        liststream = stream.split()
        self.aid = liststream[0]
        self.price = float(liststream[1])
        self.facilities = liststream[2:]


def populateHotels():

    hotels = []    
    qtde = int(f.readline())

    for index in xrange(qtde):
        hotels.append( Hotel(f.readline()))
    
    return hotels

def populateTestCases():

    tests = []    
    qtde = int(f.readline())

    for index in xrange(qtde):
        tests.append( Budgets(f.readline()))

    return tests

hotellist = populateHotels()
testlist = populateTestCases()


def getHotelWithFacilities(facilities):
    result = {}
    s1 = set(facilities)
    for hotel in hotellist:
        s2 = set(hotel.facilities)

        if s1 == s1.intersection(s2):
            result[hotel.aid] = hotel

    return result

def getHotelWithPrices(price, hotels):

    return [hotels[x] for x in hotels if hotels[x].price <= price]


def sorthotel(comp1, comp2):

    if len(comp1.facilities) > len(comp2.facilities):
        return -1
    elif len(comp1.facilities) == len(comp2.facilities):
        if comp1.price < comp2.price:
            return -1
        elif comp1.price == comp2.price:
            if comp1.aid < comp2.aid:
                return -1
            else:
                return 1
        else:
            return 1
    else:
        return 1

def executeTestCases():

    for test in testlist:
        hotelfinal = getHotelWithFacilities(test.facilities)
        hotelfinal = getHotelWithPrices(test.price, hotelfinal)

        hotelfinal = sorted(hotelfinal, sorthotel)

        output = ''
        for hotel in hotelfinal:
            output += hotel.aid + ' '

        print output

executeTestCases()