import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
from tkinter import *
from Manual_play_window import *
from battle import *
##from single import *
from game import Game
from observer import Observer
from generatorv3 import *

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
class Board:
    def __init__(self, difficulty="EASY", pits=1, rows=3, cols=3):
        self.difficulty = difficulty
        self.pits = pits
        self.gridX = rows
        self.gridY = cols
        # self.pieces = {}
        # self.selected_piece = None
        # self.focused = None
        # self.images = {}
        # self.color1 = "white"
        # self.color2 = "grey"
        # self.highlightcolor = "khaki"
        # self.dim_square = 64
class Player:
    def __init__(self, hasArrow=True, gotWumpus=False, hasGold=False):
        self.hasArrow = hasArrow
        self.gotWumpus = gotWumpus
        self.hasGold = hasGold

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        if game_state == GameState.HELP:
            board = Board()
            game_state = option_menu(screen, board)
        if game_state == GameState.NEWGAME:
            board = Board()
            game_state = option_menu(screen, board)
        if game_state == GameState.INCREASEPIT:
            if board.pits < 5:
                board.pits += 1
            game_state = option_menu(screen, board)
        if game_state == GameState.DECREASEPIT:
            if board.pits > 0:
                board.pits -= 1
            game_state = option_menu(screen, board)

        if game_state == GameState.INCREASEROW:
            if board.gridX < 6:
                board.gridX += 1
            game_state = option_menu(screen, board)
        if game_state == GameState.DECREASEROW:
            if board.gridX > 3:
                board.gridX -= 1
            game_state = option_menu(screen, board)

        if game_state == GameState.INCREASECOL:
            if board.gridY < 6:
                board.gridY += 1
            game_state = option_menu(screen, board)
        if game_state == GameState.DECREASECOL:
            if board.gridY > 3:
                board.gridY -= 1
            game_state = option_menu(screen, board)
        if game_state == GameState.NEWGAME:
            board = Board()
            game_state = option_menu(screen, board)
        if game_state == GameState.PLAYTYPE:
            game_state = choose_game(screen, board)
        if game_state == GameState.MANUAL:
            game_state = manual_play(screen, board)
        if game_state == GameState.SINGLE:
            game_state = single_play(screen, board)
        if game_state == GameState.BATTLE:
            game_state = battle_play(screen, board)
        if game_state == GameState.QUIT:
            pygame.quit()
            return

def title_screen(screen):
    title = UIElement(
        center_position=(400,200),
        font_size=70,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Wumpus World"
    )
    start_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    help_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Help",
        action=GameState.HELP
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(title, start_btn, help_btn, quit_btn)

    return game_loop(screen, buttons)

def option_menu(screen, board):
    pit_number = UIElement(
        center_position=(375, 170),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=BLACK,
        text=f"Number of pits: ({board.pits})",
    )
    increase_pit = UIElement(           #increment number of pits button
        center_position=(500, 200),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Add Pit",
        action=GameState.INCREASEPIT,
    )
    decrease_pit = UIElement(           #decrement number of pits button
        center_position=(275, 200),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Remove Pit",
        action=GameState.DECREASEPIT,
    )
    board_size = UIElement(
        center_position=(375, 270),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=BLACK,
        text=f"Board size: ({board.gridX})x({board.gridY})",
    )
    increase_row = UIElement(           #increment number of rows button
        center_position=(275, 300),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Add Row",
        action=GameState.INCREASEROW,
    )
    decrease_row = UIElement(
        center_position=(275, 325),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Remove Row",
        action=GameState.DECREASEROW,
    )
    increase_col = UIElement(
        center_position=(475, 300),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Add Column",
        action=GameState.INCREASECOL,
    )
    decrease_col = UIElement(
        center_position=(475, 325),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Remove Column",
        action=GameState.DECREASECOL,
    )
    continue_btn = UIElement(
        center_position=(375, 470),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Continue",
        action=GameState.PLAYTYPE,
    )
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    buttons = RenderUpdates(pit_number, increase_pit, decrease_pit,
    board_size, increase_row, decrease_row, increase_col, decrease_col,
    continue_btn, return_btn)
    return game_loop(screen,buttons)

def choose_game(screen,board):
    manual = UIElement(
        center_position=(425,225),
        font_size=40,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Manual Play",
        action=GameState.MANUAL,
    )
    single = UIElement(
        center_position=(425, 300),
        font_size=40,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="1 Robot Test",
        action=GameState.SINGLE,
    )
    battle = UIElement(
        center_position=(425, 375),
        font_size=40,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="8 Robot Battle",
        action=GameState.BATTLE
    )
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Back",
        action=GameState.NEWGAME,
    )

    buttons = RenderUpdates(manual, single, battle, return_btn)

    return game_loop(screen, buttons)
def manual_play(screen, board):
    root = Tk()
    canvas = Canvas(root)
    temp_new = Toplevel(canvas)
    Manual_play_window(temp_new, board)
    root.quit()
    root.mainloop()
    action=GameState.NEWGAME
    return_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Back",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = RenderUpdates(return_btn, quit_btn)
    return game_loop(screen, buttons)
def single_play(screen, board):
    #implement 1 robot version
    root = Tk()
    canvas = Canvas(root)
    temp_new = Toplevel(canvas)
    Single(temp_new, board)
    root.quit()
    root.mainloop()

    action=GameState.NEWGAME
    return_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Back",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = RenderUpdates(return_btn, quit_btn)
    return game_loop(screen, buttons)

def battle_play(screen, board):
    #implement 8 robot battle version
    root = Tk()
    canvas = Canvas(root)
    temp_new = Toplevel(canvas)
    Battle(temp_new, board)
    root.quit()
    root.mainloop()
    action=GameState.NEWGAME
    return_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Back",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = RenderUpdates(return_btn, quit_btn)
    return game_loop(screen, buttons)


def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    HELP = 2
    OPTION = 3
    INCREASEPIT = 4
    DECREASEPIT = 5
    INCREASEROW = 6
    DECREASEROW = 7
    INCREASECOL = 8
    DECREASECOL = 9
    PLAYTYPE = 10
    MANUAL = 11
    SINGLE = 12
    BATTLE = 13


if __name__ == "__main__":
    main()
