#############################################################
#Name:Sam Evans
#Date:4/12/20
#Description: Room Adventure...Revistited
############################################################
from Tkinter import *
#Room class
class Room(object):
    #constuctor
    def __init__(self, name, image):
        #room have:
        #a name
        #an image
        #exits
        #exit location
        #items and desc
        #grabbables
        #assign the name and image
        #instance variables
        self.name = name
        self.image = image
        #add dict
        self.exits = {}
        self.items = {}
        self.grabbables = []
    #Getters and Setters
    #name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    #image
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        self._image = value
    #exits
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value
    #items
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
    #grabbables
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    #add exits
    def addExit(self, exit, room):
        #add the room to the dict
        #exits = key / rooms = values
        self._exits[exit] = room
    #add items
    def addItem(self, item, description):
        #add the room to the dict
        #items = key / description = values
        self._items[item] = description
    #add grabbable item to grabbables []
    def addGrabbables(self, item):
        self._grabbables.append(item)
    #del grabbable item to grabbables []
    def delGrabbables(self, item):
        self._grabbables.remove(item)
    #custom __str__()
    def __str__(self):
        #where you are
        s = "You are in {} \n".format(self.name)
        #what you see
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"
        #exits
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "
        s += "\n"
        return s
#game class
#inherits from Frame
class Game(Frame):
    #constructor
    def __init__(self, parent):
        #call the constructor of the parent class
        Frame.__init__(self, parent)
    #create rooms
    def createRooms(self):
        #create r1-r4
        r0 = Room("the Front Yard", "room0.gif")
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        #add any items and exits
        #Front of the house
        r0.addExit("house", r1)
        #r0 item
        r0.addItem("sign", "The sign reads: 'NO TRESPASSING'")
        #r1 exits
        r1.addExit("dining_room", r2)
        r1.addExit("bedroom", r3)
        #r1 grabbables
        r1.addGrabbables("key")
        #r1 items
        r1.addItem("fireplace", "A fireplace as dead as the ghosts that haunt this mansion. inside rests a brass key. Hmm, seems useful..." )
        r1.addItem("ceiling","Cob webs drape from the ceiling. This place hasn't been visted in quite a while...") 
        #r2 exits
        r2.addExit("living_room", r1)
        r2.addExit("guest_bedroom", r4)
        #r2 items
        r2.addItem("carpet","The carpet is stained with blood...")
        r2.addItem("piano", "A piano sits on the carpet, quietly playing a tune. ")
        #r3 exits
        r3.addExit("living_room", r1)
        r3.addExit("guest_bedroom", r4)
        #r3 grabbables
        r3.addGrabbables("note")           
        #r3 items
        r3.addItem("chair","It rocks back and forth. Someone is there...")
        r3.addItem("teddy_bear", "The bear grins a little the longer you look." )
        r3.addItem("desk", "Next to the bear is a note. It seems to have something important on it.")
        #r4 exits
        r4.addExit("dining_room", r2)
        r4.addExit("bedroom", r3)
        r4.addExit("balcony", None)
        #r4 grabbables
        r4.addGrabbables("gun")
        #r4 items
        r4.addItem("safe", "Something important is in here...it has a key hole...maybe for a brass key? Type 'use' then the items name to use an item. ")
        #set the current room to r1
        Game.currentRoom = r0
        #init the player's inventory
        Game.inventory = []
    #setup GUI
    def setupGUI(self):
        #organize and pack the GUI
        self.pack(fill = BOTH, expand = 1)
        #setup player input
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side = BOTTOM, fill = X)
        Game.player_input.focus()
        #setup the image on the left of the display
        img = None
        Game.image = Label(self, width = WIDTH/2, image = img)
        Game.image.pack(side = LEFT, fill = Y)
        Game.image.pack_propagate(False) #dont let the img change the widgets size
        #setup text output on the right of the display
        text_frame = Frame(self, width = WIDTH/2)
        Game.text = Text(text_frame, bg="lightgrey",state = DISABLED)
        Game.text.pack(fill=Y,expand=1)
        text_frame.pack(side=RIGHT,fill=Y)
        text_frame.pack_propagate(False)
    #update current room image
    def setRoomImage(self):
        if(Game.currentRoom == None):
            #if you have the gun in your inventory img = win.gif. if else img = death.gif
            if Game.inventory == ["gun"]:
                Game.img = PhotoImage(file="win.gif")
            else:
                Game.img = PhotoImage(file="death.gif")
        else:
            Game.img = PhotoImage(file=Game.currentRoom.image)
        Game.image.config(image=Game.img)
        Game.image.image = Game.img
    #update status
    def setStatus(self,status):
        #clear the text widget
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)

        #if dead, say so, otherwise set the text to __str__()
        if(Game.currentRoom == None):
            #checks if gun is in inventory. If so you win if else you lose.
            if Game.inventory == ["gun"]:
                Game.text.insert(END, "YOU WON. You killed the Ghost that haunts this house. ")
            else:
                Game.text.insert(END, "The ghost that haunts the house has pushed you off the balcony. You let your guard down...better luck next time. Type 'quit' to exit. ")
        else:
            Game.text.insert(END,str(Game.currentRoom) + "You are carrying: " + str(Game.inventory)+"\n" + status)
            Game.text.config(state=DISABLED)
    #play the game
    def play(self):
        #add room
        self.createRooms()
        #setup GUI
        self.setupGUI()
        #set room image
        self.setRoomImage()
        #set status
        self.setStatus("")
    #process input
    def process(self, event):
        #set a default response
        response = "I don't understand. Try noun verb. Valid verbs are go, look, and take"
        #get the command line from GUI
        action = Game.player_input.get()
        action = action.lower()
        #handle exits
        if (action == "quit" or action == "exit"):
            exit(0)
        #handle end of game
        if (Game.currentRoom == None):
            Game.player_input.delete(0,END)
            return
        #handle verbs and nouns
        word = action.split()
        if (len(word)==2):
            verb = word[0]
            noun = word[1]
            #process enter
            #changed go to enter to flow grammatically 
            if(verb == "enter"):
                response = "Invalid exit."
                #check the currentRoom's exit
                if(noun in Game.currentRoom.exits):
                    #if it is valid, update currentRoom
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    #notify that room has changed
                    response = "Room changed"
            #process look
            elif(verb == "look"):
               #default response
                response = "I don't see that item"
                #check the cvurrentRoom's items
                if(noun in Game.currentRoom.items):
                    response = Game.currentRoom.items[noun]
            #process take
            elif(verb == "take"):
                #default response
                response = "I don't see that item."
                #check currentRoom's grabbables
                for grabbables in Game.currentRoom.grabbables:
                    #special response for the note grabbable IMPROVMENT
                    if (noun == "note"):
                        Game.inventory.append(grabbables)
                        Game.currentRoom.delGrabbables(grabbables)
                        #set response 
                        response = "The note reads: 'I AM WATCHING YOU'. "
                    #special response for gun IMPROVMENT
                    elif(noun == "gun"):
                        Game.inventory.append(grabbables)
                        Game.currentRoom.delGrabbables(grabbables)
                        #set response
                        response = "the balcony door slides open. Something is waiting for you."
                    #response for every other grabbable
                    elif(noun == grabbables):
                        Game.inventory.append(grabbables)
                        Game.currentRoom.delGrabbables(grabbables)
                        #set response
                        response = "{} grabbed".format(grabbables)
            #process use IMPROVEMENT
            elif(verb == "use"):
                #default response
                response = "item can not be used."
                for grabbables in Game.inventory:
                    if(noun == grabbables):
                        Game.inventory.remove(grabbables)
                        #set response
                        response = "{} used. A gun is in the safe with one bullet in it. Shhh, something is coming. ".format(grabbables)
                        #exit the loop
                        break
        #call the updates
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0,END)
###
#main (construct display and begin game)
#define default screen
WIDTH = 800
HEIGHT = 600
#create the window
window = Tk()
window.title("Room Adventure")
#create the GUI as a Tkinter canvas within the window
g = Game(window)
#begin the game
g.play()
#wait until the main window closes
window.mainloop()
