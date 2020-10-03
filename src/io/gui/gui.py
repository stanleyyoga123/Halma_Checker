import PySimpleGUI as sg
constant = 10

class GUI():
    def __init__(self):
        self.reverse = False
        board = [[(i,j) for j in range(constant)] for i in range(constant)]
        axis = [[sg.T("", size=(3,1))] + list(sg.T(i+1, size=(3, 1), justification='center', auto_size_text=False, text_color="white") for i in range(constant))]

        board_layout = [[sg.T(i+1, size=(2, 2), auto_size_text=True, text_color="white")] + [sg.B('', size=(4, 2), key=(i,j), pad=(0,0),focus=False, button_color=("black",self.generate_button_color((i,j))),border_width=2)
              for j in range(constant)] for i in range(constant)]

        layout = axis + board_layout
        self.window = sg.Window('Halma Checker', layout)
        self.window.Finalize() 
        

    def generate_button_color(self, position):
        if (position[0] + position[1]) % 2 == 0:
            if (position[0] + position[1]) < 4:
                return '#ffb0b0'
            elif (position[0] + position[1] > 14):
                return '#99f3bd'
            else :
                return '#e7dec8'
        else :
            if (position[0] + position[1]) < 4:
                return  '#ec0101'
            elif (position[0] + position[1] > 14):
                return '#28df99'
            else :
                return  '#cbaf87'

    def generate_reverse_button_color(self, position):
        if (position[0] + position[1]) % 2 == 0:
            if (position[0] + position[1]) > 14:
                return '#ffb0b0'
            elif (position[0] + position[1]) < 4:
                return '#99f3bd'
            else :
                return '#e7dec8'
        else :
            if (position[0] + position[1]) > 14:
                return '#ec0101'
            elif (position[0] + position[1]) < 4:
                return '#28df99'
            else :
                return '#cbaf87'

    def render(self, board):
        location = [{pawn.position.location : str(pawn)} for pawn in board.pawns]
        red_loc = [pawn.position.location for pawn in board.pawns if str(pawn) == 'R']
        green_loc = [pawn.position.location for pawn in board.pawns if str(pawn) == 'G']
        for i in range(board.b_size):
            for j in range(board.b_size):
                
                if (i,j) in red_loc:
                    self.window[(i,j)].update("♟", button_color = ("#7d0633", self.generate_button_color((i,j))), disabled=True)
                elif (i,j) in green_loc:
                    self.window[(i,j)].update('♟',  button_color = ("#557571", self.generate_button_color((i,j))), disabled=True)
                else:
                    self.window[(i,j)].update(disabled=True)
        self.window.read(timeout=10)

    def render_possible_move(self, board):
        pass 

    def remove_possible_move(self, board):
        pass 

    def input(self, board, player):
        pass 

    def render_selected_pawn(self, location):
        pass 
        

if __name__ == '__main__':
    gui = GUI()
    while True: 
        event, values = gui.window.read()
        if (type(event) == tuple):
            print(event)
        if event in (None, 'Exit'):
            gui.window.close()
            break
