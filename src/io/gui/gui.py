import PySimpleGUI as sg
import time

from src.constant import Constant 
from src.model import Color

from .utils import translate_type

class GUI():
    def __init__(self, b_size):
        self.reverse = False
        self.b_size = b_size 
        self.window = None
        self.status_window = None 
        self.board_window = None
        sg.ChangeLookAndFeel('Reddit')

    def init_loading_screen(self):
        layout = [
            [sg.T('HALMA CHECKER' + Constant.PAWNCHAR, size=(20,3), font='Any 20', justification='center')],
            [sg.ProgressBar(150, orientation='h', size=(25, 3), key='progbar')]
        ]
        self.loading_window = sg.Window('Loading Screen', layout, element_justification='center',no_titlebar=True, keep_on_top=True, grab_anywhere=False, alpha_channel=0.85)
        for i in range(150):
            event, values = self.loading_window.read(timeout=10)          
            self.loading_window['progbar'].update_bar(i + 1)
        self.loading_window.close()

    def init_game_status(self):
        layout = [
            [sg.T("Halma",size=(20,1), font='Any 30', justification='center')],
            [sg.T("Turn : ", auto_size_text=True, font='Any 20'), sg.T("0000",size=(10,1), key="turn", font='Any 20') ],
            [sg.T("Player : ", auto_size_text=True, font='Any 20'), sg.T("", key="player", size=(10,1), font="Any 20") ],
            [sg.T("Type : ", auto_size_text=True, font='Any 20'), sg.T("", key="type", size=(20,1), font="Any 20") ],
            [sg.T("Computing Time : ", auto_size_text=True, font='Any 20')],
            [sg.T("", key="time", size=(20,1), font="Any 20")]
        ]

        self.status_window = layout

    def init_game_board(self):
        button_size = (4,2) if self.b_size <= 10 else (2,1)

        board = [[(i,j) for j in range(self.b_size)] for i in range(self.b_size)]
        axis = [[sg.B('X/Y', size=button_size, pad=(0,0), disabled=True,border_width=0, focus=False, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] 
                + list(sg.B(i+1, size=button_size, pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color())) for i in range(self.b_size))]

        board_layout = [[sg.B(i+1, size=button_size, pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] 
                        + [sg.B('', size=button_size, key=(i,j), pad=(0,0),focus=False, button_color=("black",self.generate_button_color((i,j))),border_width=0)
              for j in range(self.b_size)] for i in range(self.b_size)]

        self.board_window = axis + board_layout

    def init_layout(self):
        if self.board_window is None or self.status_window is None : 
            return 
        
        self.layout = [
            [sg.Column(self.board_window), sg.VerticalSeparator(pad=(3,2)), sg.Column(self.status_window, expand_x=True, expand_y=True)],
            ]

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
    
    def show_winner(self, state):
        playerColor = state.currentPlayer.color
        color = "GREEN" if playerColor == Color.GREEN else "RED"
        p1TotalTime = "-" if repr(state.player_1.brain) == Constant.NOBRAIN else '{:.3f}'.format(state.player_1.brain.total_computing_time)   
        p2TotalTime = "-" if repr(state.player_2.brain) == Constant.NOBRAIN else '{:.3f}'.format(state.player_2.brain.total_computing_time)  
        layout = [
             [sg.T("Congratulations!!!", font="Any 20")],
             [sg.T(Constant.PAWNCHAR + str(color) + Constant.PAWNCHAR, font="Any 20",text_color= color.lower(), justification="center")],
             [sg.T("Player 1 : " + p1TotalTime + " second(s)", font="Any 15",text_color= "green", justification="center")],
             [sg.T("Player 2 : " + p2TotalTime + " second(s)", font="Any 15",text_color= "red", justification="center")],
             [sg.B('OK', font="Any 15", auto_size_button=True)]
        ]
        
        sg.Window('',layout, force_toplevel=True, no_titlebar=True, element_justification="center", keep_on_top=True).read(close=True)
        

    def render(self, state, time=None):
        if self.window is None or self.layout is None : 
            self.init_game_board()
            self.init_game_status()
            self.init_layout()
            self.window = sg.Window('Halma Checker', self.layout, force_toplevel=True, resizable=False)
            self.window.Finalize()

        # update game status
        self.window['turn'].update(state.turn + 1)
        self.window['player'].update('RED' if state.currentPlayer.color == Color.RED else 'GREEN')
        self.window['type'].update(translate_type(str(state.currentPlayer.brain)))
        
        computingTime = "-" if time == None else '{:.3f}'.format(time)
        self.window['time'].update(computingTime + " second(s)")


        location = [{pawn.position.location : str(pawn)} for pawn in state.board.pawns]
        red_loc = [pawn.position.location for pawn in state.board.pawns if str(pawn) == Constant.PAWNREDTYPE]
        green_loc = [pawn.position.location for pawn in state.board.pawns if str(pawn) == Constant.PAWNGREENTYPE]

        for i in range(state.board.b_size):
            for j in range(state.board.b_size):
                if (i,j) in red_loc:
                    self.window[(i,j)].update(Constant.PAWNCHAR, disabled_button_color = (Constant.PAWNRED, self.generate_button_color((i,j))), button_color = (Constant.PAWNRED, self.generate_button_color((i,j))), disabled=True)
                elif (i,j) in green_loc:
                    self.window[(i,j)].update(Constant.PAWNCHAR, disabled_button_color = (Constant.PAWNGREEN, self.generate_button_color((i,j))),button_color = (Constant.PAWNGREEN, self.generate_button_color((i,j))), disabled=True)
                else:
                    self.window[(i,j)].update("",disabled=True)
        self.window.read(timeout=10)

    def render_possible_move(self, board, possible_move, color):
        for i in range(board.b_size):
            for j in range(board.b_size):
                if (i, j) in possible_move:
                    self.window[(i,j)].update(Constant.TARGETCHAR, disabled=False, button_color = (Constant.NORMAL, Constant.POSSIBLERED if color == Color.RED else Constant.POSSIBLEGREEN))
        self.window.read(timeout=10)

    def remove_possible_move(self, possible_move):
        for i in range(self.b_size):
            for j in range(self.b_size):
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
                 self.remove_possible_move(possible_moves_repr)

        self.remove_possible_move(possible_moves_repr)
        return (choosed_pawn, moved_pawn)
    
