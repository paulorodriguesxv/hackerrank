"""
Problem

Identify whether four sides (given by four integers) can form a square, a rectangle, or neither.

Input: You will receive an list of strings, each containing four space-separated integers, which represent the length of the sides of a polygon. The input lines will follow the 'A B C D' order as in the following representation:

|-----A-----|
|           |
|           |
D           B
|           |
|           |
|-----C-----|
Output: A single line which contains 3 space-separated integers; representing the number of squares, number of rectangles, and number of other polygons with 4 sides. Note that squares shouldn't be counted as rectangles. Invalid polygons should also be counted as 'other polygons'.

Constraints: The four integers representing the sides will be such that: -2000 <=X <= 2000 (Where X represents the integer)

Sample Input:

36 30 36 30
15 15 15 15
46 96 90 100
86 86 86 86
100 200 100 200
-100 200 -100 200
Sample Output: 2 2 2

"""


SQUARE = 1
RECTANGLE = 2
OTHER = 3


def readPolygonsFile():
    handle = open('polygons.text', 'r')
    return [map(int, x.split()) for x in handle.readlines()]


def getShape(polygon):
    if min(polygon) <= 0:
        return OTHER

    if (polygon[0] == polygon[1] and polygon[1] == polygon[2] and polygon[2] == polygon[3]):
        return SQUARE
    elif (polygon[0] == polygon[2] and polygon[1] == polygon[3]):
        return RECTANGLE
    else:
        return OTHER

polygons = readPolygonsFile()
print polygons

polygonsResult = {}
for item in polygons:
    shape = getShape(item)
    if polygonsResult.has_key(shape):
        polygonsResult[shape] += 1
    else:
        polygonsResult[shape] = 1

print "%d %d %d " % (polygonsResult[SQUARE], polygonsResult[RECTANGLE], polygonsResult[OTHER])