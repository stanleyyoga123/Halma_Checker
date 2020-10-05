import PySimpleGUI as sg
import time

from src.constant import Constant 
from src.model import Color

class GUI():
    def __init__(self, b_size):
        self.reverse = False
        self.b_size = b_size 

    def init_loading_screen(self):
        layout = [
            [sg.T('HALMA CHECKER!!!', size=(20,3), justification='center')],
            [sg.ProgressBar(1000, orientation='h', size=(20, 3), key='progbar')]
        ]
        self.loading_window = sg.Window('Loading Screen', layout, no_titlebar=False)
        for i in range(1000):
            event, values = self.loading_window.read(timeout=5)          
            self.loading_window['progbar'].update_bar(i + 1)
        self.loading_window.close()

    def init_game_status(self):
        pass 

    def init_game_board(self):
        button_size = (4,2) if self.b_size <= 10 else (2,1)

        board = [[(i,j) for j in range(self.b_size)] for i in range(self.b_size)]
        axis = [[sg.B('X/Y', size=button_size, pad=(0,0), disabled=True,border_width=0, focus=False, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] 
                + list(sg.B(i+1, size=button_size, pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color())) for i in range(self.b_size))]

        board_layout = [[sg.B(i+1, size=button_size, pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] 
                        + [sg.B('', size=button_size, key=(i,j), pad=(0,0),focus=False, button_color=("black",self.generate_button_color((i,j))),border_width=0)
              for j in range(self.b_size)] for i in range(self.b_size)]

        layout = axis + board_layout

        self.window = sg.Window('Halma Checker', layout)
        self.window.Finalize()

    def find_mirror_end(self, b_size):
        return {
            8 : 10,
            10 : 14,
            16 : 26
        }.get(b_size)
        
    def generate_button_color(self, position):
        if (position[0] + position[1]) % 2 == 0:
            if (position[0] + position[1]) < Constant.HALFBOARDCOL:
                return Constant.LIGHTRED
            elif (position[0] + position[1]) > self.find_mirror_end(self.b_size):
                return Constant.LIGHTGREEN
            else :
                return Constant.LIGHTBOARD
        else :
            if (position[0] + position[1]) < Constant.HALFBOARDCOL:
                return  Constant.DARKRED
            elif (position[0] + position[1]) > self.find_mirror_end(self.b_size):
                return Constant.DARKGREEN
            else :
                return  Constant.DARKBOARD

    def render(self, state):
        print ("Game Status : ")
        print(f"Current Player : {str(state.currentPlayer)}")
        print(f"Current Turn : {state.turn }")
        location = [{pawn.position.location : str(pawn)} for pawn in state.board.pawns]
        red_loc = [pawn.position.location for pawn in state.board.pawns if str(pawn) == Constant.PAWNREDTYPE]
        green_loc = [pawn.position.location for pawn in state.board.pawns if str(pawn) == Constant.PAWNGREENTYPE]
        for i in range(state.board.b_size):
            for j in range(state.board.b_size):
                if (i,j) in red_loc:
                    self.window[(i,j)].update(Constant.PAWNCHAR, button_color = (Constant.PAWNRED, self.generate_button_color((i,j))), disabled=True)
                elif (i,j) in green_loc:
                    self.window[(i,j)].update(Constant.PAWNCHAR, button_color = (Constant.PAWNGREEN, self.generate_button_color((i,j))), disabled=True)
                else:
                    self.window[(i,j)].update(disabled=True)
        self.window.read(timeout=10)

    def render_possible_move(self, board, possible_move, color):
        for i in range(board.b_size):
            for j in range(board.b_size):
                if (i, j) in possible_move:
                    self.window[(i,j)].update(Constant.TARGETCHAR, disabled=False, button_color = (Constant.NORMAL, Constant.POSSIBLERED if color == Color.RED else Constant.POSSIBLEGREEN))
        self.window.read(timeout=10)

    def remove_possible_move(self, board, possible_move):
        for i in range(board.b_size):
            for j in range(board.b_size):
                if (i, j) in possible_move:
                    self.window[(i,j)].update("", disabled=True, button_color=(Constant.NORMAL, self.generate_button_color((i,j))))
        

    def input(self, state):
        if state.currentPlayer.color == Color.RED:
            loc = [pawn.position.location for pawn in state.board.pawns if str(pawn) == Constant.PAWNREDTYPE]
        else : 
            loc = [pawn.position.location for pawn in state.board.pawns if str(pawn) == Constant.PAWNGREENTYPE]

        for i in range(state.board.b_size):
            for j in range(state.board.b_size):
                if (i,j) in loc:
                    self.window[(i,j)].update(disabled=False)
        event, values = self.window.read()
        while True:
            if event in (None, "Exit"):
                raise RuntimeError("Exit Games!")
            
            choosed_pawn = None
            if event in loc:
                choosed_pawn = [pawn for pawn in state.board.pawns if pawn.position.location == event][0]
                possible_moves = state.board.possible_moves(choosed_pawn)
                possible_moves_repr = [pawn.position.location for pawn in possible_moves]
                self.render_possible_move(state.board, possible_moves_repr, state.currentPlayer.color)

            event, values = self.window.read()
            if event in (None, "Exit"):
                raise RuntimeError("Exit Games!")

            moved_pawn = None
            if event in possible_moves_repr:
                moved_pawn = possible_moves[possible_moves_repr.index(event)]
                break
            else : 
                 self.remove_possible_move(state.board, possible_moves_repr)

        self.remove_possible_move(state.board, possible_moves_repr + [choosed_pawn.position.location])
        return (choosed_pawn, moved_pawn)
    
