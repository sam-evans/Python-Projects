        ##################################################################################################################################################
#Name:Sam Evans
#Date:3/28/20
#Description:Chaos Game (Sierpinski Triangle)
##################################################################################################################################################
from Tkinter import *
from random import randint
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

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
        POINT_COLOR = ["red", "black"]
        POINT_RADIUS = [0, 2]
        def __init__(self, master):
                Canvas.__init__(self, master, bg = "white")
                self.pack(fill = BOTH, expand = 1)
        def plotPoints(self, n):
                #initial vertices
                vertices = [Point(MIN_X, MAX_Y), Point(MAX_X, MAX_Y), Point(MID_X, MIN_Y)]
                points = []
                #plots the 3 vertices in vertices list
                for i in(vertices):
                        
                        self.plot2(i)
                #calculates the midpont of the 3 vertices
                midpt = vertices[0].midpt(vertices[1])
                points.append(midpt)
                self.plot(midpt)
                #calculates the midpoint of random vertices and plots
                for i in range (n):
                        midpt2 = points[-1].midpt(vertices[randint(0,(len(vertices)-1))])
                        points.append(midpt2)
                        self.plot(midpt2)
        def plot(self, other):
                #color points black with a Radius of 0
                color = self.POINT_COLOR[1]
                self.create_oval(other.x, other.y, other.x + self.POINT_RADIUS[0] * 2, other.y + self.POINT_RADIUS[0] * 2, outline=color, fill=color)
        def plot2(self, other):
                #color points red with Radius of 2
                color = self.POINT_COLOR[0]
                self.create_oval(other.x, other.y, other.x + self.POINT_RADIUS[1] * 2, other.y + self.POINT_RADIUS[1] * 2, outline=color, fill=color)
####################################B######################################################################################################
#main
#window size
WIDTH = 600
HEIGHT = 520
#number of points
NUM_POINTS = 50000
# Min, Mid, and Max x & y values
MIN_X = 5 
MAX_X = 595
MIN_Y = 5
MAX_Y = 515
MID_X = (MIN_X + MAX_X)/2
#tk window 
window = Tk()
window.geometry("{}x{}".format(WIDTH,HEIGHT))

s = ChaosGame(window)
s.plotPoints(NUM_POINTS)
window.mainloop()
