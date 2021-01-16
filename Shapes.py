######################################################################################################################
# Name:Sam Evans
# Date:4/8/20
# Description:Shapes
######################################################################################################################
#Shape super class
class Shape(object):
    #constructor for height and width
    def __init__(self, height, width):
    #range checker for r2 (0,0)
        if (height <= 0):
            height = 1
        self.height = height
        if (width <= 0):
            width = 1
        self.width = width
        
    #decorators
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
        
    @property
    def width(self):
        return self._width
    
    #range checker for p1 width being negative
    @width.setter
    def width(self, value):
        if(value < 0):
            pass
        else:
            self._width = value
            
    #magic string function that will be inherited 
    def __str__(self):
        return ("* " * self.height + "\n") * self.width
    
#Retangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, width, height)
        
#Square class
class Square(Shape):
    def __init__(self, width):
        Shape.__init__(self, width, width)
        
#Triangle class
class Triangle(Shape):
    def __init__(self, width):
        Shape.__init__(self, width, width)
        
    #Triangle recursion 
    def __str__(self):
        x = self.width
        while x > 0:
            print ("* " * x)
            x -= 1
            #range check for when x hits 0
            if (x == 0):
                return (" ")
        
#Parallelogram class
class Parallelogram(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, width, height)
        
    #Parallelogram recursion 
    def __str__(self):
        x = self.width
        empstr = "* " * self.height
        while x > 0:
            print (" " * (x - 1)) + empstr
            x -= 1
            #range check for when x hits 0
            if (x <= 0):
                return str("")

    
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print r1
s1 = Square(6)
print s1
t1 = Triangle(7)
print t1
p1 = Parallelogram(10, 3)
print p1
r2 = Rectangle(0, 0)
print r2
p1.width = 2
p1.width = -1
p1.height = 2
print p1

