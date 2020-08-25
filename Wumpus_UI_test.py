import tkinter as tk
import platform
import os
# from PIL import Image, ImageTk
CELL_SIZE = 32 # the pixel for a single square for play board
from Manual_play_window import *
ROOT_DIR = "."

class Start_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        if platform.system() == "Darwin":  ### if its a Mac
            self.button1 = tk.Button(self.frame, text='Manual Play', width=25, command=self.new_window1, highlightbackground='#3E4149')
            self.button2 = tk.Button(self.frame, text='1 robot test', width=25, command=self.new_window2, highlightbackground='#3E4149')
            self.button3 = tk.Button(self.frame, text='8 robots battle', width=25, command=self.new_window3, highlightbackground='#3E4149')
        else:
            self.button1 = tk.Button(self.frame, text='Manual Play', width=25, command=self.new_window1)
            self.button2 = tk.Button(self.frame, text='1 robot test', width=25, command=self.new_window2)
            self.button3 = tk.Button(self.frame, text='8 robots battle', width=25, command=self.new_window3)

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.frame.pack()

    def new_window1(self): # manual play button
        self.temp_new = tk.Toplevel(self.master)
        self.app = Manual_play_window(self.temp_new, data)

    def new_window2(self): # 1 robot test button
        self.temp_new = tk.Toplevel(self.master)
        self.app = One_robot_window(self.temp_new)

    def new_window3(self): # 8 robot battle button
        self.temp_new = tk.Toplevel(self.master)
        self.app = Robot_battle_window(self.temp_new)

    def close_windows(self):
        self.master.destory()

# class Manual_play_window:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.widgets()
#
#         self.rows = 10
#         self.columns = 10
#         self.size = CELL_SIZE
#         self.color1 = 'white'
#         self.color2 = 'grey'
#         self.pieces = {}
#
#         canvas_width = self.columns * self.size
#         canvas_height = (self.rows) * self.size
#
#         self.canvas = tk.Canvas(self.master, borderwidth=0, highlightthickness=0,
#                                 width=canvas_width, height=canvas_height, background="bisque")
#         self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
#
#         # this binding will cause a refresh if the user interactively
#         # changes the window size
#         self.canvas.bind("<Configure>", self.refresh)
#         self.frame.pack()
#
#         # menubar = tk.Menu(self.master)
#         # menu_setting = tk.Menu(menubar, tearoff=0)
#         # menubar.add_cascade(label="setting", menu=menu_setting)
#         # menu_setting.add_command(label="new game", command=self.menu_action)
#         # menu_setting.add_command(label="load game", command=self.menu_action)
#         # menu_setting.add_command(label="restart game", command=self.menu_action)
#         # menu_setting.add_separator()
#         # menu_setting.add_command(label="Quit", command = self.master.destory)
#         #
#         # self.master.config(menu=menubar)
#         # img_right = ImageTk.PhotoImage(Image.open(os.path.join(ROOT_DIR,"img_src","btn_right.png")).convert("RGB").resize((20,20)))
#         # btn_right = tk.Button(self.master, image = img_right, command =self.move_right())
#         # btn_right = tk.Button(self.master, image = tk.PhotoImage(file = r"./img_src/btn_right.png"), command =self.move_right())
#
#         btn_right = tk.Button(self.master, text="test", command =self.move_right()).pack()
#         # btn_right.place(x=50, y=self.rows * self.size+100)
#
#         # btn_test = tk.Button(self.master, text= "test", command = self.move_right()).place(x=50, y=self.rows * self.size+100)
#
#     def widgets(self):
#         menubar = tk.Menu(root)
#         menubar.add_command(label="File")
#         # menubar.add_command(label="Quit", command=root.quit())
#
#         root.config(menu=menubar)
#
#     def menu_action(self):
#         print("hit menu")
#
#     def move_right(self):
#         print("hit right")
#     # credit to https://stackoverflow.com/questions/4954395/create-board-game-like-grid-in-python
#     def addpiece(self, name, image, row=0, column=0):
#         '''Add a piece to the playing board'''
#         self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
#         self.placepiece(name, row, column)
#
#     def placepiece(self, name, row, column):
#         '''Place a piece at the given row/column'''
#         self.pieces[name] = (row, column)
#         x0 = (column * self.size) + int(self.size / 2)
#         y0 = (row * self.size) + int(self.size / 2)
#         self.canvas.coords(name, x0, y0)
#
#     def refresh(self, event):
#         '''Redraw the board, possibly in response to window being resized'''
#         xsize = int((event.width - 1) / self.columns)
#         ysize = int((event.height - 1) / self.rows)
#         self.size = min(xsize, ysize)
#         self.canvas.delete("square")
#         color = self.color2
#         for row in range(self.rows):
#             color = self.color1 if color == self.color2 else self.color2
#             for col in range(self.columns):
#                 x1 = (col * self.size)
#                 y1 = (row * self.size)
#                 x2 = x1 + self.size
#                 y2 = y1 + self.size
#                 self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
#                 color = self.color1 if color == self.color2 else self.color2
#         for name in self.pieces:
#             self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
#         self.canvas.tag_raise("piece")
#         self.canvas.tag_lower("square")
#
#     def update_board(self):
#         return NotImplementedError
#
#     def close_windows(self):
#         self.master.destory()

class One_robot_window:
    def __init__(self, master):
        return NotImplementedError
    def close_windows(self):
        self.master.destory()

class Robot_battle_window:
    def __init__(self, master):
        return NotImplementedError
    def close_windows(self):
        self.master.destory()

def init(data):
    data.states = ["home", "help", "input", "playType"]
    data.curState = data.states[0]
    data.width = 1000
    data.height = 800
    data.difficulty = "EASY"
    data.pits = "1"
    data.gridSize = "8x8"
    data.playType = ""
    data.gridX = 3
    data.gridY = 7

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chess")


    class Struct(object): pass
    data = Struct()
    init(data)
    gui = Manual_play_window(root, data)
    root.mainloop()


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Manual_play_window(root)
#     # app = Start_window(root)
#
#     root.mainloop()
