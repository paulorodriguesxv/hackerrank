import math
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(object):

    def __init__(self, a, b, r):   
        self.a = a
        self.b = b
        self.r = r
    
    def calculate(self, point):
       return ((point.x - self.a) ** 2) + ((point.y - self.b)**2) <= self.r**2

class Rectangle(object):

    def __init__(self, point1, point2):   
        self.point1 = point1
        self.point2 = point2
        self.coords = self.get_coords()
    
    def get_coords(self):
        cx = (self.point1.x + self.point2.x) / 2
        cy = (self.point1.y + self.point2.y) / 2

        vx = self.point1.x - cx
        vy = self.point1.y - cy

        ux = vy
        uy = vx

        x3 = cx + ux
        y3 = cy + uy

        x4 = cx - ux
        y4 = cy - uy

        print ((self.point1.x, self.point1.y), (x3,y3), (self.point2.x, self.point2.y), (x4,y4))
        return ((self.point1.x, self.point1.y), (x3,y3), (self.point2.x, self.point2.y), (x4,y4))


    def point_reta(self, x, y, pointA, pointB):
        #print pointA, pointB
        x1, y1 = pointA
        x2, y2 = pointB

        if x2 == x1:
            return False
        
        dap = math.sqrt((x - x1)**2 + (y - y1)**2)
        dab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        dbp = math.sqrt((x -x2)**2 + (y - y2)**2)
    
        m = (y2 - y1) / ( x2 - x1)


        res = (-m*x + y + m*x1 - y1 == 0) and (dap <= dab) and (dbp <= dab)

        if res and False:
            print dap, dab, dbp
            print x, y
            print pointA, pointB
        return res

    def point_inside_polygon(self, x,y,poly):

        n = len(poly)
        inside =False
        inte = 0 
        p1x,p1y = poly[0]

        for i in range(n+1):        
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):                    
                        if p1y != p2y:                        
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                            inte += 1
                        if (p1x == p2x or x <= xinters):
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside
    
    def calculate(self, point):    
        return self.point_inside_polygon(point.x, point.y, self.coords) or \
                self.point_reta(point.x, point.y, self.coords[0], self.coords[1]) or \
                self.point_reta(point.x, point.y, self.coords[1], self.coords[2]) or \
                self.point_reta(point.x, point.y, self.coords[3], self.coords[0]) or \
                self.point_reta(point.x, point.y, self.coords[2], self.coords[3]) 

class Canvas(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self, circle, rectangle):

        for h in xrange(self.h):
            line = ""
            for w in xrange(self.w):
                point = Point(w, h)
                if circle.calculate(point):
                    line += "#"                
                elif rectangle.calculate(point):
                    line += "#"
                else:                
                    line += "."
            print line


def belongs_pixel(canvas, point):    
    x_point = (point.x >= canvas.x - 0.5) and (point.x <= canvas.x + 0.5)
    y_point = (point.y >= canvas.y - 0.5) and (point.y <= canvas.y + 0.5)

canvas = Canvas(20, 16)
circle = Circle(9,6,5)
rectangle = Rectangle(Point(16,14), Point(8,14))
canvas.draw(circle, rectangle)



def point_reta(x, y, pointA, pointB):

    x1, y1 = pointA
    x2, y2 = pointB

    if x2 == x1:
        return False
    
    dap = math.sqrt((x - x1)**2 + (y - y1)**2)
    dab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


    m = (y2 - y1) / ( x2 - x1)

    return -m*x + y + m*x1 - y1 == 0 


print point_reta(7, 15, (8, 14), (12, 10))    