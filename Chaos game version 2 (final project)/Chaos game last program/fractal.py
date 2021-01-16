from math import *
#2D Point class
class Point(object):
    def __init__ (self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    #Decorators 
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
    #Distance Formula
    def dist(self, other):
        delta_x = (self._x) - (other._x)
        delta_y = (self._y) - (other._y)
        return (delta_x ** 2 + delta_y ** 2) ** 0.5
    #Midpoint formula
    def midpt(self, other):
        x_co = (self._x + other._x)/2
        y_co = (self._y + other._y)/2
        return Point(x_co, y_co)
    #Magic string function  
    def __str__(self):
        return ("({}), ({})").format(self.x, self.y)
    #interpt function
    def interpt(self, other, r):
        #make sure the dist ratio is expressed from a smaller comp
        #to a larger one
        #first the x-comp
        rx = r
        if(self.x > other.x):
            rx = 1.0 - r
        #y-comp
        ry = r
        if(self.y > other.y):
            ry = 1.0 - r
        x = abs(self.x - other.x) * rx + min(self.x, other.x)
        y = abs(self.y - other.y) * ry + min(self.y, other.y)
        return Point(x, y)
#Fractal Super-class
class Fractal(object):
    def __init__(self, dimensions):
        #the canvas dimensions
	self.dimensions = dimensions
	#the default number of points to plot 50,000
	self.num_points = 50000
	#default distance ratio .5
	self.r = 0.5
	self.vertices = []
    #Takes the distance ratio as input and returns the x-coordinate on the canvas that corresponds with the distance ratio input
    def frac_x(self, r):
	return int((self.dimensions["max_x"] - self.dimensions["min_x"]) * r) + self.dimensions["min_x"]
    #Takes the distance ratio as input and returns the y-coordinate on the canvas that corresponds with the distance ratio input
    def frac_y(self, r):
	return int((self.dimensions["max_y"] - self.dimensions["min_y"]) * r) + self.dimensions["min_y"]
#SierpinskiTriangle sub-class 
class SierpinskiTriangle(Fractal):
    def __init__(self, dimensions):
	#inherits the fractal class
	Fractal.__init__(self, dimensions)
    def makeTri(self):
	#appends the vertices to the verticies list in the Fractal class
	self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["min_y"]))
	self.vertices.append(Point(self.dimensions["min_x"],self.dimensions["max_y"]))
	self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["max_y"]))
#SierpinskiCarpet sub-class
class SierpinskiCarpet(Fractal):
    def __init__(self, dimensions):
	#inherits the fractal class
	Fractal.__init__(self, dimensions)
	#changes the default num_points value to 100000
	self.num_points = 100000
	#changes the default distance ratio to 0.66
	self.r = 0.66
    def makeCarpet(self):
	#appends the vertices to the verticies list in the Fractal class
	self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["min_y"]))
	self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["min_y"]))
	self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["min_y"]))
	self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["mid_y"]))
	self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["mid_y"]))
	self.vertices.append(Point(self.dimensions["min_x"], self.dimensions["max_y"]))
	self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["max_y"]))
	self.vertices.append(Point(self.dimensions["max_x"], self.dimensions["max_y"]))
#Pentagon sub-class
class Pentagon(Fractal):
    def __init__(self, dimensions):
	#inherits the fractal class
	Fractal.__init__(self, dimensions)
	#changes the default distance ratio to 0.618
	self.r = 0.618
    def makePentagon(self):
	#appends the vertices to the verticies list in the Fractal class
	self.vertices.append(Point(self.dimensions["mid_x"] + (self.dimensions["mid_x"]*cos(2 * pi/5 + 60)), (self.frac_y(0.5375))+(self.dimensions["mid_y"] * sin(2*pi/5+60))))
	self.vertices.append(Point(self.dimensions["mid_x"] + (self.dimensions["mid_x"]*cos(4 * pi/5 + 60)), (self.frac_y(0.5375))+(self.dimensions["mid_y"] * sin(4*pi/5+60))))
	self.vertices.append(Point(self.dimensions["mid_x"] + (self.dimensions["mid_x"]*cos(6 * pi/5 + 60)), (self.frac_y(0.5375))+(self.dimensions["mid_y"] * sin(6*pi/5+60))))
	self.vertices.append(Point(self.dimensions["mid_x"] + (self.dimensions["mid_x"]*cos(8 * pi/5 + 60)), (self.frac_y(0.5375))+(self.dimensions["mid_y"] * sin(8*pi/5+60))))
	self.vertices.append(Point(self.dimensions["mid_x"] + (self.dimensions["mid_x"]*cos(10 * pi/5 + 60)), (self.frac_y(0.5375))+(self.dimensions["mid_y"] * sin(10*pi/5+60))))
#Hexagon sub-class
class Hexagon(Fractal):
    def __init__(self, dimensions):
	#inherits the fractal class
	Fractal.__init__(self, dimensions)
	#changes the default distance ratio to 0.665
	self.r = 0.665
    def makeHexagon(self):
	#appends the vertices to the verticies list in the Fractal class
	self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["min_y"]))
	self.vertices.append(Point(self.dimensions["min_x"], self.frac_y(0.25)))
	self.vertices.append(Point(self.dimensions["max_x"], self.frac_y(0.25)))
	self.vertices.append(Point(self.dimensions["min_x"], self.frac_y(0.75)))
	self.vertices.append(Point(self.dimensions["max_x"], self.frac_y(0.75)))
	self.vertices.append(Point(self.dimensions["mid_x"], self.dimensions["max_y"]))
#Octagon sub-class
class Octagon(Fractal):
    def __init__(self, dimensions):
        #inherits the fractal class
        Fractal.__init__(self, dimensions)
        #changes the default num_points value to 75000
        self.num_points = 75000
        #changes the default distance ratio to 0.7075
        self.r = 0.705
    def makeOctagon(self):
        #appends the vertices to the verticies list in the Fractal class
        self.vertices.append(Point(self.frac_x(0.2925), self.dimensions["min_y"]))
        self.vertices.append(Point(self.frac_x(0.7075), self.dimensions["min_y"]))
        self.vertices.append(Point(self.dimensions["min_x"], self.frac_y(0.2925)))
        self.vertices.append(Point(self.dimensions["max_x"], self.frac_y(0.2925)))
        self.vertices.append(Point(self.dimensions["min_x"], self.frac_y(0.7075)))
        self.vertices.append(Point(self.dimensions["max_x"], self.frac_y(0.7075)))
        self.vertices.append(Point(self.frac_x(0.2925), self.dimensions["max_y"]))
        self.vertices.append(Point(self.frac_x(0.7075), self.dimensions["max_y"]))
