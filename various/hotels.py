

from collections import Counter

#f = open('hotels.txt')

words = raw_input().split()
reviewsSize = int(raw_input())
class Hotel:
    def __init__(self, words, hotelid, review):
        self.words = words
        self.hotelid = hotelid
        self.review = review

    def getWords(self):
        #print review
        counter = Counter([x for x in self.review if x in self.words])

        return sum(counter.values())

hotelList = {}
for i in xrange(reviewsSize):

    hotelid = raw_input().replace("\n", "")
    review = raw_input().replace("\n", "").replace(".", "").replace(",", "").lower()

    if not hotelList.has_key(hotelid):
        hotelList[hotelid] = Hotel(words, hotelid, review.split())
    else:
        hotelList[hotelid].review.extend(review.split()) 

    
def byWords(hotel):
    return hotel.getWords()

hotelResult = [hotelList[x] for x in hotelList]

hotelSorted = sorted(hotelResult, key=byWords, reverse=True)


print ' '.join([x.hotelid for x in hotelSorted])
