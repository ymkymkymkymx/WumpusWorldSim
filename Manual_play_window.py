import tkinter as tk
from copy import deepcopy
from game import Game
from observer import Observer
from generatorv3 import *


CELL_SIZE = 64

class Board(dict):
    y_axis = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z')
    x_axis = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
    captured_pieces = {'white': [], 'black': []}
    player_turn = None
    halfmove_clock = 0
    fullmove_number = 1
    history = []

    # def __init__(self, pat=None):
        # self.show(START_PATTERN)

    def is_in_check_after_move(self, p1, p2):
        tmp = deepcopy(self)
        tmp.move(p1, p2)
        return tmp.king_in_check(self[p1].color)

    def shift(self, p1, p2):
        p1, p2 = p1.upper(), p2.upper()
        piece = self[p1]
        try:
            dest = self[p2]
        except:
            dest = None
        if self.player_turn != piece.color:
            raise NotYourTurn("Not " + piece.color + "'s turn!")
        enemy = ('white' if piece.color == 'black' else 'black')
        moves_available = piece.moves_available(p1)
        if p2 not in moves_available:
            raise InvalidMove
        if self.all_moves_available(enemy):
            if self.is_in_check_after_move(p1, p2):
                raise Check
        if not moves_available and self.king_in_check(piece.color):
            raise CheckMate
        elif not moves_available:
            raise Draw
        else:
            self.move(p1, p2)
            self.complete_move(piece, dest, p1, p2)

    def move(self, p1, p2):
        piece = self[p1]
        del self[p1]
        self[p2] = piece

    def complete_move(self, piece, dest, p1, p2):
        enemy = ('white' if piece.color == 'black' else 'black')
        if piece.color == 'black':
            self.fullmove_number += 1
        self.halfmove_clock += 1
        self.player_turn = enemy
        abbr = piece.shortname
        if abbr == 'P':
            abbr = ''
            self.halfmove_clock = 0
        if dest is None:
            movetext = abbr + p2.lower()
        else:
            movetext = abbr + 'x' + p2.lower()
            self.halfmove_clock = 0
        self.history.append(movetext)

    def all_moves_available(self, color):

        result = []
        for coord in self.keys():
            if (self[coord] is not None) and self[coord].color == color:
                moves = self[coord].moves_available(coord)
                if moves: result += moves
        return result

    def occupied(self, color):
        result = []

        for coord in iter(self.keys()):
            if self[coord].color == color:
                result.append(coord)
        return result



class ChessError(Exception): pass


class Check(ChessError): pass


class InvalidMove(ChessError): pass

class InvalidDifficulty(ChessError): pass

class CheckMate(ChessError): pass


class Draw(ChessError): pass


class NotYourTurn(ChessError): pass


class Manual_play_window:
    pieces = {}
    selected_piece = None
    focused = None
    images = {}
    color1 = "white"
    color2 = "grey"
    highlightcolor = "khaki"
    rows = 8
    columns = 8
    dim_square = CELL_SIZE

    def __init__(self, parent, data):
        self.rows = data.gridX
        self.columns = data.gridY
        self.fire = False
        self.observer = None
        self.data = data
        self.game = self.init_game_with_data(data)
        # print(data.gridX)  #todo parse data

        self.chessboard = Board()
        self.parent = parent
        # Adding Top Menu
        self.menubar = tk.Menu(parent)
        self.side_menu = tk.Menu(self.menubar, tearoff=0)
        self.side_menu.add_command(label="restart", command=self.restart_game)
        self.side_menu.add_command(label ="new game", command=self.new_game)
        self.side_menu.add_command(label="load script", command=self.load_script)
        self.side_menu.add_command(label="quit", command=self.quit)
        self.menubar.add_cascade(label="Game", menu=self.side_menu)
        self.parent.config(menu=self.menubar)
        self.buttons = ["move_up", "move_down",  "move_left", "move_right",
                        "shoot_up", "shoot_down", "shoot_left", "shoot_right"]

        self.map_icon = self.get_map_icon()


        # Adding Frame
        self.btmfrm = tk.Frame(parent, height=64)
        self.info_label = tk.Label(self.btmfrm,
                                   text="tap arrow bottoms to start",
                                   fg=self.color2)
        self.info_label.pack(side=tk.RIGHT, padx=8, pady=5)
        self.btmfrm.pack(fill="x", side=tk.BOTTOM)

        canvas_width = (self.columns) * self.dim_square
        canvas_height = (self.rows + 1.5) * self.dim_square
        gap_size = 30
        if self.columns < 7:
            canvas_width = 6 * self.dim_square
            gap_size = 10
        self.canvas = tk.Canvas(parent, width=canvas_width,
                                height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

        self.button_pos = [
            [0, self.dim_square * self.rows + gap_size, self.dim_square, self.dim_square * (self.rows + 1) + gap_size],
            [0 + gap_size + self.dim_square, self.dim_square * self.rows + gap_size,
             self.dim_square + gap_size + self.dim_square, self.dim_square * (self.rows + 1) + gap_size],
            [0 + (gap_size + self.dim_square) * 2, self.dim_square * self.rows + gap_size,
             self.dim_square + (gap_size + self.dim_square) * 2, self.dim_square * (self.rows + 1) + gap_size],
            [0 + (gap_size + self.dim_square) * 3, self.dim_square * self.rows + gap_size,
             self.dim_square + (gap_size + self.dim_square) * 3, self.dim_square * (self.rows + 1) + gap_size],
            [0 + (gap_size + self.dim_square) * 4, self.dim_square * self.rows + gap_size,
             self.dim_square + (gap_size + self.dim_square) * 4, self.dim_square * (self.rows + 1) + gap_size]]

        # self.draw_board()
        self.canvas.bind("<Button-1>", self.square_clicked)
        self.draw_board()
        self.draw_pieces()

    def init_game_with_data(self, data):
        o1 = Observer()
        sizex = data.gridX
        sizey = data.gridY
        pits = int(data.pits)
        diffy = self.num_difficulty(data.difficulty)
        start_invis_board = tolistofset(findmap(sizex, sizey, pits, diffy), sizex, sizey)
        g1 = Game()
        g1.subscribeObserver(o1)
        g1.startGame(start_invis_board)
        self.observer = o1
        return g1

    def num_difficulty(self, difficulty):
        if difficulty == "EASY":
            return 1
        elif difficulty == "MEDIUM":
            return 2
        elif difficulty == "HARD":
            return 3
        else:
            return InvalidDifficulty
    # TODO
    def new_game(self):
        print("NOT IMPLEMENTED")

    def quit(self):
        print("NOT IMPLEMENTED")

    def load_script(self):
        print("NOT IMPLEMENTED")

    def restart_game(self, pop = None):
        if not pop == None:
            pop.destory()
        self.game = self.init_game_with_data(self.data)
        self.draw_board()
        self.draw_pieces()
        self.info_label.config(text="   press button to start the Game  ", fg='red')

    def square_clicked(self, event):
        self.draw_board()

        if event.y > self.dim_square*self.rows:
            self.click_manual_button(event.x, event.y)

            self.info_label["text"] = self.observer.history
            if self.observer.Fail:
                self.draw_lose()

    def get_map_icon(self):
        map_file_name = ['map_glitter.png','map_gold.png','map_pit.png',
                         'map_smell.png','map_wind.png', 'map_wumpus.png', 'map_robot.png','btn_fire.png']
        map_key_name = ["Glitter","Gold","Pit",
                        "Stench","Breeze","LiveWumpus", "robot", "Arrow"]
        map_icon = {}
        for i in range(len(map_file_name)):
            map_icon[map_key_name[i]] = tk.PhotoImage(file='img_src/'+map_file_name[i])
        return map_icon


    def draw_board(self):
        color = self.color2
        for row in range(self.rows):
            # color = self.color1 \
            #     if color == self.color2 else self.color2
            for col in range(self.columns):
                color = self.color1 \
                    if color == self.color2 else self.color2
                x1 = (col * self.dim_square)
                y1 = (row * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                if (self.focused is not None and (row, col) in self.focused):
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=self.highlightcolor,
                                                 tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color,
                                                 tags="area")
                # color = self.color1 \
                #     if color == self.color2 else self.color2
        self.draw_manual_button()

        for name in self.pieces:
            self.pieces[name] = (self.pieces[name][0], self.pieces[name][1])
            x0 = (self.pieces[name][1] * self.dim_square) + int(
                self.dim_square / 2)
            y0 = ((7 - self.pieces[name][0]) * self.dim_square) + int(
                self.dim_square / 2)
            self.canvas.coords(name, x0, y0)

        # self.draw_manual_button()
        self.canvas.tag_raise("test")
        self.canvas.tag_raise("area")
        self.canvas.tag_raise("occupied")
        self.canvas.tag_lower("area")

    def draw_manual_button(self):
        btn_file_name = ['img_src/btn_up.png', 'img_src/btn_down.png', 'img_src/btn_left.png', 'img_src/btn_right.png',
                         'img_src/btn_fire.png']
        for i in range(0, 5):
            filename = btn_file_name[i]
            self.canvas.create_rectangle(self.button_pos[i][0], self.button_pos[i][1], self.button_pos[i][2],
                                         self.button_pos[i][3],
                                         fill="white", tags="area")
            self.images[filename] = tk.PhotoImage(file=filename)
            self.canvas.create_image(self.button_pos[i][0]+32, self.button_pos[0][1]+32, image=self.images[filename])

    def click_manual_button(self, x, y):
        for i in range(0,5):
            x1, y1, x2, y2 = self.button_pos[i][0], self.button_pos[i][1], self.button_pos[i][2], self.button_pos[i][3]
            if x1<x<x2 and y1<y<y2:
                if i == 4:
                    self.fire = not self.fire
                    if self.fire:
                        self.canvas.create_rectangle(self.button_pos[4][0], self.button_pos[4][1],
                                                     self.button_pos[4][2],
                                                     self.button_pos[4][3],
                                                     fill="red", tags="area")
                        self.canvas.create_image(self.button_pos[i][0] + 32, self.button_pos[0][1] + 32,
                                                 image=self.images['img_src/btn_fire.png'])
                else:
                    if self.fire:
                        self.parse_button(self.game, self.buttons[i + 4])
                        self.fire = not self.fire
                        print("press fire", self.buttons[i + 4])
                    else:
                        print(self.buttons[i] + " pressed")
                        self.parse_button(self.game, self.buttons[i])

        self.draw_pieces()

    def parse_button(self, g1, nextMove):
        if nextMove == "move_up":
            g1.moveRobotUp()
        elif nextMove == "move_down":
            g1.moveRobotDown()
        elif nextMove == "move_left":
            g1.moveRobotLeft()
        elif nextMove == "move_right":
            g1.moveRobotRight()
        elif nextMove == "shoot_up":
            g1.shootArrowUp()
        elif nextMove == "shoot_down":
            g1.shootArrowDown()
        elif nextMove == "shoot_right":
            g1.shootArrowRight()
        elif nextMove == "shoot_left":
            g1.shootArrowLeft()
        else:
            return InvalidMove

    def draw_pieces(self):
        self.canvas.delete("occupied")
        # self.canvas.create_image(32, 32, image=self.map_icon["LiveWumpus"],
        #                                  tags="occupied")
        x, y = self.game.robot_position[0], self.game.robot_position[1]

        for i in range(self.rows):
            for j in range(self.columns):
                x0 = (j * self.dim_square) + int(self.dim_square / 2)
                y0 = (i * self.dim_square) + int(self.dim_square / 2)
                if len(self.game.visible_board[self.rows - i - 1][j]) == 0 and (self.rows - i - 1 != x or j != y):
                    # self.canvas.create_image(32, 32, image=self.map_icon["LiveWumpus"],
                    #                                  tags="occupied")
                    pass
                elif not (self.rows - i - 1 != x or j != y):
                    self.canvas.create_image(x0,y0, image=self.map_icon["robot"],
                                                 tags="occupied")
                else:
                    temp = self.game.visible_board[self.rows - i - 1][j].difference({}).pop()
                    if temp == "Arrow" or temp == 'DeadWumpus':
                        self.check_win_with_arrow()
                        if len(self.observer.history)>0 and self.observer.history[-1] == "MISSED-WUMPUS":
                            self.canvas.create_image(x0, y0, image=self.map_icon[temp],
                                             tags="occupied")
                        elif len(self.observer.history) > 0 and self.observer.history[-1] == "SUCCESS":
                            self.draw_win()
                        else:
                            self.canvas.create_image(x0, y0, image=self.map_icon["LiveWumpus"],
                                                     tags="occupied")
                    else:
                        self.canvas.create_image(x0, y0, image=self.map_icon[temp],
                                                 tags="occupied")

    def check_win_with_arrow(self):
        if self.observer.history[-1] == "MISSED-WUMPUS": #if missed the shoot
            # self.draw_lose()
            return
        else:
            #self.draw_win() # no miss then win
            return
    def draw_win(self):
        self.end_pop_window("Congratuations!", "YOU KILLED WUMPUS!")
        self.restart_game()
        print("win")

    def draw_lose(self):
        if self.observer.history[-1] == "LIVE-WUMPUS":
            self.end_pop_window("LOSE", "KILLED BY WUMPUS")
        else:
            self.end_pop_window("LOSE", "Wanna try again?")
        self.restart_game()
        print("lost")

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

    def end_pop_window(self, title, label):
        pop = tk.Toplevel()
        pop.title(title)
        l = tk.Label(pop, text = label)
        l.grid(row=0, column=0)
        b = tk.Button(pop, text="Okay!", command=pop.destroy)
        b.grid(row=2, column=0)
