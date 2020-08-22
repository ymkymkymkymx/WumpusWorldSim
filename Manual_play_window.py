CELL_SIZE = 32
from tkinter import *
from PIL import Image, ImageTk
import os

class Manual_play_window:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        # self.cell_size = CELL_SIZE

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

        temp_img = ImageTk.PhotoImage(Image.open('./test.png'))
        self.pieces["test"] = temp_img

        self.frame.pack()

        # img_right = ImageTk.PhotoImage(Image.open(os.path.join(ROOT_DIR,"img_src","btn_right.png")).convert("RGB").resize((20,20)))
        # btn_right = tk.Button(self.master, image = img_right, command =self.move_right())
        # btn_right = tk.Button(self.master, image = tk.PhotoImage(file = r"./img_src/btn_right.png"), command =self.move_right())

        # btn_right = tk.Button(self.master, text = 'tst', command =self.move_right())
        # btn_right.place(x=50, y=self.rows * self.size+100)

        # btn_test = tk.Button(self.master, text= "test", command = self.move_right()).place(x=50, y=self.rows * self.size+100)
        # temp_img = ImageTk.PhotoImage(Image.open(os.path.join(".","img_src","btn_right.png")))
        # btn_test = Button(self.master, image = temp_img, command=self.move_right()).place(x=50, y=self.rows * self.size+100)

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
            # ImageTk.PhotoImage(Image.open('./test.png'))

        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def update_board(self):
        return NotImplementedError

    def close_windows(self):
        self.master.destroy()