from Tkinter import *
from fractal import *
from random import randint
class ChaosGame(Canvas):
    def __init__(self,master):
        Canvas.__init__(self, master, bg = "white")
        self.pack(fill = BOTH, expand = 1)
        #dimensions dict
        self.dimensions = {}
        #vertex default radus and color
        self.VERTEX_RADIUS = 2
        self.VERTEX_COLOR = "red"
        #points default radius and color
        self.POINT_RADIUS = 0
        self.POINT_COLOR = "black"
    def make(self,f):
        #dimensions dict keys/values
        self.dimensions["min_x"] = 5
        self.dimensions["max_x"] = WIDTH - 5
        self.dimensions["min_y"] = 5
        self.dimensions["max_y"] = HEIGHT - 5
        self.dimensions["mid_x"] = (self.dimensions["min_x"] + self.dimensions["max_x"])/2
        self.dimensions["mid_y"] = (self.dimensions["min_y"] + self.dimensions["max_y"])/2
        #runs loops according to strings in the FRACTALS list
        if (f == "SierpinskiTriangle"):
            #creates an instace of SierpinksiTriangle class
            create = SierpinskiTriangle(self.dimensions)
            points = []
            create.makeTri()
            #plots the vertices in color RED and radius 2 
            for i in range(len(create.vertices)):
                self.plot_points(create.vertices[i], self.VERTEX_COLOR, self.VERTEX_RADIUS)
            midpt = create.vertices[0].interpt(create.vertices[1], create.r)
            points.append(midpt)
            #plots the rest of the points in BLACK and radius of 0
            for i in range(create.num_points):
                midpt2 = points[-1].interpt(create.vertices[randint(0,(len(create.vertices)-1))], create.r)
                points.append(midpt2)
                self.plot_points(midpt2, self.POINT_COLOR, self.POINT_RADIUS)
        elif(f == "SierpinskiCarpet"):
            #creates an instace of SierpinskiCarpet class
            create = SierpinskiCarpet(self.dimensions)
            points = []
            create.makeCarpet()
            #plots the vertices in color RED and radius 2 
            for i in range(len(create.vertices)):
                self.plot_points(create.vertices[i], self.VERTEX_COLOR, self.VERTEX_RADIUS)
            midpt = create.vertices[0].interpt(create.vertices[1], create.r)
            points.append(midpt)
            #plots the rest of the points in BLACK and radius 0
            for i in range(create.num_points):
                midpt2 = points[-1].interpt(create.vertices[randint(0,(len(create.vertices)-1))], create.r)
                points.append(midpt2)
                self.plot_points(midpt2, self.POINT_COLOR, self.POINT_RADIUS)
        elif(f == "Pentagon"):
            #creates an instance of Pentagon class
            create = Pentagon(self.dimensions)
            points = []
            create.makePentagon()
            #plots the vertices in color RED with radius 2 
            for i in range(len(create.vertices)):
                self.plot_points(create.vertices[i], self.VERTEX_COLOR, self.VERTEX_RADIUS)
            midpt = create.vertices[0].interpt(create.vertices[1], create.r)
            points.append(midpt)
            #plots the rest of the points in BLACK with a radius 0
            for i in range(create.num_points):
                midpt2 = points[-1].interpt(create.vertices[randint(0,(len(create.vertices)-1))], create.r)
                points.append(midpt2)
                self.plot_points(midpt2, self.POINT_COLOR, self.POINT_RADIUS)
        elif(f == "Hexagon"):
            #creates an instace of the Hexagon class
            create = Hexagon(self.dimensions)
            points = []
            create.makeHexagon()
            #plots the vertices in color RED with a radius of 2
            for i in range(len(create.vertices)):
                self.plot_points(create.vertices[i], self.VERTEX_COLOR, self.VERTEX_RADIUS)
            midpt = create.vertices[0].interpt(create.vertices[1], create.r)
            points.append(midpt)
            #plots the rest of the points in color BLACK with a radius of 0
            for i in range(create.num_points):
                midpt2 = points[-1].interpt(create.vertices[randint(0,(len(create.vertices)-1))], create.r)
                points.append(midpt2)
                self.plot_points(midpt2, self.POINT_COLOR, self.POINT_RADIUS)
        else:
            #creates an instace of the Octagon class
            create = Octagon(self.dimensions)
            points = []
            create.makeOctagon()
            #plots the vertices in color RED with a radius of 2
            for i in range(len(create.vertices)):
                self.plot_points(create.vertices[i], self.VERTEX_COLOR, self.VERTEX_RADIUS)
            midpt = create.vertices[0].interpt(create.vertices[1], create.r)
            points.append(midpt)
            #plots the rest of the points in color BLACK with a radius of 0
            for i in range(create.num_points):
                midpt2 = points[-1].interpt(create.vertices[randint(0,(len(create.vertices)-1))], create.r)
                points.append(midpt2)
                self.plot_points(midpt2, self.POINT_COLOR, self.POINT_RADIUS)
    #plots the dots in the GUI with correct radius and color
    def plot_points(self, point, color, radius):
        self.create_oval(point.x, point.y, point.x + radius * 2, point.y + radius * 2, outline=color, fill=color)
##################################################
#main
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
#the implemented fractals
FRACTALS = ["SierpinskiTriangle", "SierpinskiCarpet", "Pentagon", "Hexagon", "Octagon"]
#create the fractals in individual (sequential) windows
for f in FRACTALS:
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("The Chaos Game...Reloaded")
    #create the game as a Tkinter canvas inside the window
    s = ChaosGame(window)
    s.make(f)
    #wait for the window to close
    window.mainloop()
