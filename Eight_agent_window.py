import tkinter as tk
from copy import deepcopy
from game import Game
from observer0 import Observer
from generatorv3 import *
import AgentGame
import time
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


class Single_agent_window:
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

    def __init__(self, parent, data,agentclass,themap):
        self.agentclass=agentclass
        self.themap=themap
        self.rows = len(themap)
        self.columns = len(themap[0])
        self.fire = False
        self.observer = None
        self.data = data
        self.game=[]
        self.aggame = self.init_game_with_data(data)
        self.steps=0
        # print(data.gridX)  #todo parse data

        self.chessboard = Board()
        self.parent = parent
        # Adding Top Menu
        #self.menubar = tk.Menu(parent)
        #self.side_menu = tk.Menu(self.menubar, tearoff=0)
        #self.side_menu.add_command(label="restart", command=self.restart_game)
        #self.side_menu.add_command(label ="new game", command=self.new_game)
        #self.side_menu.add_command(label="load script", command=self.load_script)
        #self.side_menu.add_command(label="quit", command=self.quit)
        #self.menubar.add_cascade(label="Game", menu=self.side_menu)
        #self.parent.config(menu=self.menubar)
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

        canvas_width = (self.columns) * self.dim_square * 4
        canvas_height = (self.rows + 1.5) * self.dim_square * 3
        gap_size = 30
        gap_size = 30
        if self.columns < 7:
            canvas_width = 6 * self.dim_square * 5
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
        #self.stepthroughgame()
    '''
    def stepthroughgame(self):
        while not self.aggame.g.finished:
            self.aggame.step()
            self.draw_board()
            self.draw_pieces()
            time.sleep(0.5)
    '''
    def init_game_with_data(self, data):
        games=[]
        self.game=[]
        for aclass in self.agentclass:
            o1 = Observer()
            
            sizex = self.rows
            sizey = self.columns
            agent=aclass.Agent(sizex,sizey)
            pits = int(data.pits)
            diffy = self.data.diffy
            game1=AgentGame.AgentGame(sizex,sizey,pits,diffy,agent,o1)
            game1.setboard(self.themap)
            self.game.append(game1.g)
            games.append(game1)
        return games

    def num_difficulty(self, difficulty):
        if difficulty == "EASY":
            return 1
        elif difficulty == "MEDIUM":
            return 2
        elif difficulty == "HARD":
            return 3
        else:
            return 0
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
        self.aggame = self.init_game_with_data(self.data)
        self.draw_board()
        self.draw_pieces()
        self.info_label.config(text="   press button to start the Game  ", fg='red')
        self.canvas.update()        
        
    def square_clicked(self, event):
        self.draw_board()

        if event.y > self.dim_square*self.rows:
            self.click_manual_button(event.x, event.y)
            '''
            self.info_label["text"] = self.observer.history
            if self.observer.Fail:
                self.draw_lose()
            '''

    def get_map_icon(self):
        map_file_name = ['map_glitter.png','map_gold.png','map_pit.png',
                         'map_smell.png','map_wind.png', 'map_wumpus.png', 'map_robot.png','btn_fire.png','map_smellwind.png','map_deadwumpus.png']
        map_key_name = ["Glitter","Gold","Pit",
                        "Stench","Breeze","LiveWumpus", "robot", "Arrow","StenchBreeze","DeadWumpus"]
        map_icon = {}
        for i in range(len(map_file_name)):
            map_icon[map_key_name[i]] = tk.PhotoImage(file='img_src/'+map_file_name[i])
        return map_icon

    def draw_board(self):
        self.canvas.delete("occupied")
        one_board_width = (self.columns * self.dim_square)
        one_board_height = (self.rows + 1.5) * self.dim_square
        start_x = start_y = 0
        for i in range(8):
            if i == 4:
                start_x = 0
                start_y += one_board_height + 25
            self.draw_board_helper(start_x, start_y)
            start_x += one_board_width + 25 #gap 
        self.draw_manual_button()
    def draw_board_helper(self, start_x, start_y):
        color = self.color2

        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.dim_square + start_x)
                y1 = (row * self.dim_square + start_y)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                if (self.focused is not None and (row, col) in self.focused):
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=self.highlightcolor,
                                                 tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color,
                                                 tags="area")
                color = self.color1 if color == self.color2 else self.color2
        # self.draw_manual_button()

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
        btn_file_name = ['img_src/btn_right.png','img_src/btn_fire.png']
        for i in range(len(btn_file_name)):
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
                        self.parse_button( self.buttons[i + 4])
                        self.fire = not self.fire
                        print("press fire", self.buttons[i + 4])
                    else:
                        print(self.buttons[i] + " pressed")
                        self.parse_button( self.buttons[i])

        self.draw_pieces()

    def parse_button(self, nextMove):
        ##self.aggame.step()
        if nextMove == "move_up":
            f=False
            count=0
            while not f and count<1000:
                for aggame in self.aggame:            
                    if not aggame.g.finished:
                        aggame.step()
                f=True
                for g in self.game:
                    f=f and g.finished
                
                self.draw_board()
                self.draw_pieces()
                self.canvas.update()
                self.steps+=1
                time.sleep(0.5)
                count+=1
            self.checkwin()
        elif nextMove == "move_down":
            for aggame in self.aggame:            
                if not aggame.g.finished:
                    aggame.step()
                    
            self.draw_board()
            self.draw_pieces()
            self.canvas.update()
            self.steps+=1
            f=True
            for g in self.game:
                f=f and g.finished
            if f:                
                self.checkwin()            
            
        
    def checkwin(self):
        f=True
        for g in self.game:
            f=f and g.finished
        if f:
            for i in range(8):
                if self.aggame[i].win:
                    print("Agent {0:} win with {1:} steps".format(i+1,self.aggame[i].stepcount))
                else:
                    print("Agent {0:} lose".format(i+1))
            a=input("finished")
            self.draw_win()
            
    def draw_pieces(self):
        one_board_width = (self.columns * self.dim_square)
        one_board_height = (self.rows + 1.5) * self.dim_square
        start_x = start_y = 0        
        for i in range(8):
            if i == 4:
                start_x = 0
                start_y += one_board_height + 25
            self.draw_pieces_helper(start_x,start_y,self.game[i])
            start_x += one_board_width + 25 #gap 
    def draw_pieces_helper(self,inix,iniy,thegame):
        
        x, y = thegame.robot_position[0], thegame.robot_position[1]
        for i in range(self.rows):
            for j in range(self.columns):
                x0 = (j * self.dim_square) + int(self.dim_square / 2)+inix
                y0 = (i * self.dim_square) + int(self.dim_square / 2)+iniy
                for temp in thegame.invisible_board[self.rows - i - 1][j]:
                    if temp == "LiveWumpus":
                        self.canvas.create_image(x0, y0, image=self.map_icon["LiveWumpus"],
                                                    tags="occupied")
                    if temp =="Pit":
                        self.canvas.create_image(x0, y0, image=self.map_icon["Pit"],
                                                    tags="occupied")
                    if temp == "Gold":
                        self.canvas.create_image(x0, y0, image=self.map_icon["Gold"],
                                                    tags="occupied")
                if len(thegame.visible_board[self.rows - i - 1][j]) == 0 :
                    pass
                
                else:
                    temp = thegame.visible_board[self.rows - i - 1][j].difference({}).pop()
                    if temp == "Arrow" or temp == 'DeadWumpus':
                        self.canvas.create_image(x0, y0, image=self.map_icon["DeadWumpus"],
                                                     tags="occupied")
                    else:
                        brz=False
                        stc=False
                        for msg in thegame.visible_board[self.rows - i - 1][j]:
                            if msg =="Stench":
                                stc=True
                            if msg=="Breeze":
                                brz=True
                        if stc and brz:
                            self.canvas.create_image(x0, y0, image=self.map_icon["StenchBreeze"],
                                                     tags="occupied")                            
                        else:
                            self.canvas.create_image(x0, y0, image=self.map_icon[temp],
                                                 tags="occupied")
                if not (self.rows - i - 1 != x or j != y):
                    self.canvas.create_image(x0,y0, image=self.map_icon["robot"],
                                                         tags="occupied")                


    def draw_win(self):
        self.end_pop_window("Congratuations!", "Finished after {0} steps!".format(self.steps+1))
        
        print("win")
        self.restart_game()
        

    def draw_lose(self):
        self.end_pop_window("LOSE", "Wanna try again?")
        
        print("lost")
        self.restart_game()

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
