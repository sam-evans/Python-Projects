######################################################################################################################
# Name: Sam Evans 
# Date: 3-15-20
# Description: 2D Points
######################################################################################################################

# the 2D point class
class Point(object):
	# write your code for the point class here (and subsequently remove this comment)
	def __init__ (self, x = 0.0, y = 0.0):
		self.x = float(x)
		self.y = float(y)

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

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4) 
# display them
print ("p1:", p1)
print ("p2:", p2)
print ("p3:", p3)
# calculate and display some distances
print ("distance from p1 to p2:", p1.dist(p2))
print ("distance from p2 to p3:", p2.dist(p3))
print ("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print ("midpt of p1 and p2:", p1.midpt(p2))
print ("midpt of p2 and p3:", p2.midpt(p3))
print ("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print ("p4:", p4)
print ("distance from p4 to p1:", p4.dist(p1))
