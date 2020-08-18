import math, random, time, copy
from tkinter import *
import sys, os
from PIL import Image, ImageTk
CELL_SIZE = 32 # the pixel for a single square for play board

class Manual_play_window:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.rows = 10
        self.columns = 10
        self.size = CELL_SIZE
        self.color1 = 'white'
        self.color2 = 'grey'
        self.pieces = {}

        canvas_width = self.columns * self.size + 500
        canvas_height = self.rows * self.size + 500

        self.canvas = Canvas(self.master, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)
        self.frame.pack()

        # img_right = ImageTk.PhotoImage(Image.open(os.path.join(ROOT_DIR,"img_src","btn_right.png")).convert("RGB").resize((20,20)))
        # btn_right = tk.Button(self.master, image = img_right, command =self.move_right())
        # btn_right = tk.Button(self.master, image = tk.PhotoImage(file = r"./img_src/btn_right.png"), command =self.move_right())

        # btn_right = tk.Button(self.master, text = 'tst', command =self.move_right())
        # btn_right.place(x=50, y=self.rows * self.size+100)

        # btn_test = tk.Button(self.master, text= "test", command = self.move_right()).place(x=50, y=self.rows * self.size+100)


    def move_right(self):
        print("hit right")
    # credit to https://stackoverflow.com/questions/4954395/create-board-game-like-grid-in-python
    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size / 2)
        y0 = (row * self.size) + int(self.size / 2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def update_board(self):
        return NotImplementedError

    def close_windows(self):
        self.master.destroy()

class One_robot_window:
    def __init__(self, master):
        return NotImplementedError
    def close_windows(self):
        self.master.destroy()

class Robot_battle_window:
    def __init__(self, master):
        return NotImplementedError
    def close_windows(self):
        self.master.destroy()

def init(data):
    data.states = ["home", "help", "input", "playType"]
    data.curState = data.states[0]
    data.width = 1000
    data.height = 800
    data.difficulty = "  "
    data.pits = "   "
    data.gridSize = "   "
    data.playType = ""
    data.gridX = 0
    data.gridY = 0

def redrawAll(canvas, data):
    if (data.curState == "home"):
        homeScreenRedraw(canvas, data)
    if (data.curState == "input"):
        inputScreenRedraw(canvas, data)
    if (data.curState == "playType"):
        playTypeScreenRedraw(canvas, data)


def mousePressed(event, data):
    if (data.curState == "home"):
        homeMousePressed(event, data)
    if (data.curState == "input"):
        inputMousePressed(event,data)
    if (data.curState == "playType"):
        playTypeMousePressed(event, data)
    #Add a back button


def homeMousePressed(event, data):
    mouseX = event.x
    mouseY = event.y
    if(280 < mouseX < 740 and 340 < mouseY < 500): #click Start!
        data.curState = data.states[2]

    if(370 < mouseX < 640 and 540 < mouseY < 640): #click Help
        data.curState = data.states[1]


def homeScreenRedraw(canvas, data):
    canvas.create_rectangle(0,0, data.width,data.height, fill ="light blue", width = 0)
    # canvas.create_image(0,0, image=data.image0, anchor =NW)
    canvas.create_text(500, 200, text = "Wumpus World", font = "Helvetica 55 bold italic")
    canvas.create_rectangle(280,340,740,500,fill = "white",width = 10,outline ='#a79eff')
    canvas.create_text(505,420,text = "Start!", font = "Helvetica 46 bold italic")

    canvas.create_rectangle(370, 540, 640, 640, fill = "white", width = 5, outline = "#a79eff")
    canvas.create_text(500, 590, text = "Help", font = "Helvetica 26 bold italic")

def difficultyMousePressed(event,data):
    mouseX = event.x
    mouseY = event.y

    if (350 < mouseX < 650 and 200 < mouseY < 300):
        data.curState = data.states[3]
    if (350 < mouseX < 650 and 400 < mouseY < 500):
        data.curState = data.states[4]
    if (350 < mouseX < 650 and 600 < mouseY < 600):
        data.curState = data.states[5]

def difficultyScreenRedraw(canvas, data):
    canvas.create_rectangle(0,0, data.width,data.height, fill ="white", width = 0)
    canvas.create_text(500, 100, text = "Select Your Difficulty Level", font = "Helvetica 40 bold italic")
    canvas.create_rectangle(350, 200, 650, 300, fill = "white", width = 5)
    canvas.create_text(500, 250, text = "Easy", font = "Helvetica 35 bold italic")
    canvas.create_rectangle(350, 400, 650, 500, fill = "white", width = 5)
    canvas.create_text(500, 450, text = "Medium", font = "Helvetica 35 bold italic")
    canvas.create_rectangle(350, 600, 650, 700, fill = "white", width = 5)
    canvas.create_text(500, 650, text = "Hard", font = "Helvetica 35 bold italic")
def inputMousePressed(event, data):
    mouseX = event.x
    mouseY = event.y
    #Clicking a difficulty level
    if (80 <= mouseY <= 155):
        if (225 <= mouseX <= 375):
            data.difficulty = "EASY"
        elif (425 <= mouseX <= 575):
            data.difficulty = "MEDIUM"
        elif (625 <= mouseX <= 775):
            data.difficulty = "HARD"
    #Clicking number of pits
    elif (240 <= mouseY <= 300):
        if (270 <= mouseX <= 330):
            data.pits = "1"
        elif (370 <= mouseX <= 430):
            data.pits = "2"
        elif (470 <= mouseX <= 530):
            data.pits = "3"
        elif (570 <= mouseX <= 630):
            data.pits = "4"
        elif (670 <= mouseX <= 730):
            data.pits = "5"
    #clicking size of board
    elif (390 <= mouseY <= 450):
        if (270 <= mouseX <= 330):
            data.gridSize = "3x3"
            data.gridX = 3
            data.gridY = 3
        elif (370 <= mouseX <= 430):
            data.gridSize = "3x4"
            data.gridX = 3
            data.gridY = 4
        elif (470 <= mouseX <= 530):
            data.gridSize = "3x5"
            data.gridX = 3
            data.gridY = 5
        elif (570 <= mouseX <= 630):
            data.gridSize = "3x6"
            data.gridX = 3
            data.gridY = 6
        elif (670 <= mouseX <= 730):
            data.gridSize = "4x4"
            data.gridX = 4
            data.gridY = 4
    elif (490 <= mouseY <= 550):
        if (270 <= mouseX <= 330):
            data.gridSize = "4x5"
            data.gridX = 4
            data.gridY = 5
        elif (370 <= mouseX <= 430):
            data.gridSize = "4x6"
            data.gridX = 4
            data.gridY = 6
        elif (470 <= mouseX <= 530):
            data.gridSize = "5x5"
            data.gridX = 5
            data.gridY = 5
        elif (570 <= mouseX <= 630):
            data.gridSize = "5x6"
            data.gridX = 5
            data.gridY = 6
        elif (670 <= mouseX <= 730):
            data.gridSize = "6x6"
            data.gridX = 5
            data.gridY = 6
    elif (600 <= mouseY <= 650):
        if (450 <= mouseX <= 555):
            data.curState = data.states[3]


def inputScreenRedraw(canvas, data):
    canvas.create_rectangle(0,0, data.width,data.height, fill ="light blue", width = 0)
    #Select Difficulty Level
    canvas.create_text(500,50, text="Select your difficulty level", font="Helvetica 20 italic")
    canvas.create_rectangle(225,80,375,155, fill="white", width=5)  #easy
    canvas.create_text(300, 110, text = "Easy", font = "Helvetica 25 bold italic")
    canvas.create_rectangle(425,80,575,155, fill="white", width=5)  #medium
    canvas.create_text(500, 110, text = "Medium", font = "Helvetica 25 bold italic")
    canvas.create_rectangle(625,80,775,155, fill="white", width=5)  #hard
    canvas.create_text(700, 110, text = "Hard", font = "Helvetica 25 bold italic")

    #Select Number of Pits
    canvas.create_text(500,200, text="Select the number of pits", font="Helvetica 20 italic")
    canvas.create_rectangle(270,240,330,300, fill="white", width=5)
    canvas.create_text(300, 270, text = "1", font = "Helvetica 25 bold italic")
    canvas.create_rectangle(370,240,430,300, fill="white", width=5)
    canvas.create_text(400, 270, text = "2", font = "Helvetica 25 bold italic")
    canvas.create_rectangle(470,240,530,300, fill="white", width=5)
    canvas.create_text(500, 270, text = "3", font = "Helvetica 25 bold italic")
    canvas.create_rectangle(570,240,630,300, fill="white", width=5)
    canvas.create_text(600, 270, text = "4", font = "Helvetica 25 bold italic")
    canvas.create_rectangle(670,240,730,300, fill="white", width=5)
    canvas.create_text(700, 270, text = "5", font = "Helvetica 25 bold italic")

    #Select Board Size
    canvas.create_text(500,350, text="Select the desired board size", font="Helvetica 20 italic")
    #First Row
    canvas.create_rectangle(270,390,330,450, fill="white", width=5)
    canvas.create_text(300, 420, text = "3x3", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(370,390,430,450, fill="white", width=5)
    canvas.create_text(400, 420, text = "3x4", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(470,390,530,450, fill="white", width=5)
    canvas.create_text(500, 420, text = "3x5", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(570,390,630,450, fill="white", width=5)
    canvas.create_text(600, 420, text = "3x6", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(670,390,730,450, fill="white", width=5)
    canvas.create_text(700, 420, text = "4x4", font = "Helvetica 20 bold italic")
    #Second Row
    canvas.create_rectangle(270,490,330,550, fill="white", width=5)
    canvas.create_text(300, 520, text = "4x5", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(370,490,430,550, fill="white", width=5)
    canvas.create_text(400, 520, text = "4x6", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(470,490,530,550, fill="white", width=5)
    canvas.create_text(500, 520, text = "5x5", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(570,490,630,550, fill="white", width=5)
    canvas.create_text(600, 520, text = "5x6", font = "Helvetica 20 bold italic")
    canvas.create_rectangle(670,490,730,550, fill="white", width=5)
    canvas.create_text(700, 520, text = "6x6", font = "Helvetica 20 bold italic")

    #Submit Button
    canvas.create_rectangle(450,600,555,650, fill="deep sky blue", width=5)
    canvas.create_text(500, 625,text="Submit", font = "Helvetica 20 bold italic")

    selectionText= "Selected: Difficulty - {0}  Pits - {1}  Size - {2}".format(data.difficulty, data.pits, data.gridSize)
    canvas.create_text(500,700, text=selectionText, font="Helvetica 20 bold italic")


def new_window1(canvas): # manual play button
    temp_new = Toplevel(canvas)
    app = Manual_play_window(temp_new)

def new_window2(canvas): # 1 robot test button
    temp_new = Toplevel(canvas)
    app = One_robot_window(temp_new)

def new_window3(canvas): # 8 robot battle button
    temp_new = Toplevel(canvas)
    app = Robot_battle_window(temp_new)

def close_windows(canvas):
    canvas.destroy()

def playTypeMousePressed(event, data):
    mouseX = event.x
    mouseY = event.y
    if (350 < mouseX < 650 and 200 < mouseY < 300):
        data.playType = "manual"
    if (350 < mouseX < 650 and 400 < mouseY < 500):
        data.playType = "single"
    if (350 < mouseX < 650 and 600 < mouseY < 600):
        data.playType = "battle"
def playTypeScreenRedraw(canvas, data):
    canvas.create_rectangle(0,0, data.width,data.height, fill ="light blue", width = 0)
    canvas.create_text(500, 100, text = "Select Your Play Type", font = "Helvetica 40 bold italic")
    canvas.create_rectangle(330, 200, 670, 300, fill = "white", width = 5)
    canvas.create_text(500, 250, text = "Manual Play", font = "Helvetica 35 bold italic")
    canvas.create_rectangle(330, 400, 670, 500, fill = "white", width = 5)
    canvas.create_text(500, 450, text = "1 Robot Test", font = "Helvetica 35 bold italic")
    canvas.create_rectangle(330, 600, 670, 700, fill = "white", width = 5)
    canvas.create_text(500, 650, text = "8 Robot Battle", font = "Helvetica 35 bold italic")
    if(data.playType == "manual") :
        new_window1(canvas)
    elif (data.playType == "single"):
        new_window2(canvas)
    elif (data.playType == "battle"):
        new_window3(canvas)

def run():
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0,0, data.width, data.height, fill="white", width=0)
        redrawAll(canvas, data)
        canvas.update()
    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    class Struct(object): pass
    data = Struct()
    root = Tk()
    root.title("Wumpus World")
    root.resizable(False,False) #prevents resizing window
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    #set up events
    root.bind("<Button-1>", lambda event: mousePressedWrapper(event, canvas, data))



    root.mainloop()


# Driver code
if(__name__=="__main__"):
	run()
