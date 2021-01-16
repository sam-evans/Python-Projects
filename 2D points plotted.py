######################################################################################################################
# Name: Sam Evans 
# Date: 3/21/20
# Description: 2D Points...Plotted
######################################################################################################################
from Tkinter import *
from random import randint
# the 2D point class
class Point(object):
	def __init__ (self, x = 0.0, y = 0.0):
		self.x = (x)
		self.y = (y)

	

	def dist(self, other):
		delta_x = (self._x) - (other._x)
		delta_y = (self._y) - (other._y)
		return (delta_x ** 2 + delta_y ** 2) ** 0.5

	def midpt(self, other):
		x_co = (self._x + other._x)/2
		y_co = (self._y + other._y)/2
		return Point(x_co, y_co)
	
	def __str__(self):
		return ("{}, {}").format(self.x, self.y)
# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
	#local variables
	POINT_COLOR = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "orange"]
	POINT_RADIUS = 0
	def __init__(self, master):
		#create canvas 
		Canvas.__init__(self, master, bg="white")
		self.pack(fill=BOTH, expand=1)
	
	def plotPoints(self, n):
		#plot points
		for i in range (n):
			x = randint(0, WIDTH - 1)
			y = randint(0, HEIGHT - 1)
			self.plot(Point(x,y))
	def plot(self, other):
		#randomly color points and draw dots
		color = self.POINT_COLOR[randint(0, len(self.POINT_COLOR)-1)]
		self.create_oval(other.x, other.y, other.x + self.POINT_RADIUS *2, other.y + self.POINT_RADIUS * 2, outline=color, fill=color)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
