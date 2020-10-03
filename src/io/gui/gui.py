import PySimpleGUI as sg

from src.constant import Constant 
from src.model import Color

class GUI():
    def __init__(self):
        self.reverse = False
        board = [[(i,j) for j in range(Constant.BOARDSIZE)] for i in range(Constant.BOARDSIZE)]
        axis = [[sg.T("", size=(3,2))] + list(sg.B(i+1, size=(4, 2), pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color())) for i in range(Constant.BOARDSIZE))]

        board_layout = [[sg.B(i+1, size=(3, 2), pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] + [sg.B('', size=(4, 2), key=(i,j), pad=(0,0),focus=False, button_color=("black",self.generate_button_color((i,j))),border_width=0)
              for j in range(Constant.BOARDSIZE)] for i in range(Constant.BOARDSIZE)]

        layout = axis + board_layout
        self.window = sg.Window('Halma Checker', layout)
        self.window.Finalize() 
        

    def generate_button_color(self, position):
        if (position[0] + position[1]) % 2 == 0:
            if (position[0] + position[1]) < 4:
                return Constant.LIGHTRED
            elif (position[0] + position[1] > 14):
                return Constant.LIGHTGREEN
            else :
                return Constant.LIGHTBOARD
        else :
            if (position[0] + position[1]) < 4:
                return  Constant.DARKRED
            elif (position[0] + position[1] > 14):
                return Constant.DARKGREEN
            else :
                return  Constant.DARKBOARD

    def render(self, board):
        location = [{pawn.position.location : str(pawn)} for pawn in board.pawns]
        red_loc = [pawn.position.location for pawn in board.pawns if str(pawn) == Constant.PAWNREDTYPE]
        green_loc = [pawn.position.location for pawn in board.pawns if str(pawn) == Constant.PAWNGREENTYPE]
        for i in range(board.b_size):
            for j in range(board.b_size):
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
                    self.window[(i,j)].update(Constant.TARGETCHAR, disabled=False, button_color = ("black", Constant.POSSIBLERED if color == Color.RED else Constant.POSSIBLEGREEN))
        self.window.read(timeout=10)

    def remove_possible_move(self, board, possible_move):
        for i in range(board.b_size):
            for j in range(board.b_size):
                if (i, j) in possible_move:
                    self.window[(i,j)].update("", disabled=True, button_color=("black", self.generate_button_color((i,j))))
        

    def input(self, board, player):
        if player.color == Color.RED:
            loc = [pawn.position.location for pawn in board.pawns if str(pawn) == Constant.PAWNREDTYPE]
        else : 
            loc = [pawn.position.location for pawn in board.pawns if str(pawn) == Constant.PAWNGREENTYPE]

        for i in range(board.b_size):
            for j in range(board.b_size):
                if (i,j) in loc:
                    self.window[(i,j)].update(disabled=False)
        event, values = self.window.read()
        while True:
            if event in (None, "Exit"):
                raise RuntimeError("Exit Games!")
            
            choosed_pawn = None
            if event in loc:
                choosed_pawn = [pawn for pawn in board.pawns if pawn.position.location == event][0]
                possible_moves = board.possible_moves(choosed_pawn)
                possible_moves_repr = [pawn.position.location for pawn in possible_moves]
                self.render_possible_move(board, possible_moves_repr, player.color)

            event, values = self.window.read()
            if event in (None, "Exit"):
                raise RuntimeError("Exit Games!")

            moved_pawn = None
            if event in possible_moves_repr:
                moved_pawn = possible_moves[possible_moves_repr.index(event)]
                break
            else : 
                 self.remove_possible_move(board, possible_moves_repr)

        self.remove_possible_move(board, possible_moves_repr + [choosed_pawn.position.location])
        return (choosed_pawn, moved_pawn)
    
if __name__ == '__main__':
    gui = GUI()
    while True: 
        event, values = gui.window.read()
        if (type(event) == tuple):
            print(event)
        if event in (None, 'Exit'):
            gui.window.close()
            break
