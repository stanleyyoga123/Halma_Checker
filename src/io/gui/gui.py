import PySimpleGUI as sg
constant = 10

class GUI():
    def __init__(self):
        self.reverse = False
        board = [[(i,j) for j in range(constant)] for i in range(constant)]
        axis = [[sg.T("", size=(2,1))] + list(sg.T(i+1, size=(3, 1), auto_size_text=False, text_color="white") for i in range(constant))]

        board_layout = [[sg.T(i+1, size=(2, 2), auto_size_text=True, text_color="white")] + [sg.B('', size=(4, 2), key=(i,j), pad=(0,0), button_color=self.generate_button_color((i,j))) 
              for j in range(constant)] for i in range(constant)]

        layout = axis + board_layout
        self.window = sg.Window('Halma Checker', layout)
        self.window.Finalize() 
        

    def generate_button_color(self, position):
        if (position[0] + position[1]) % 2 == 0:
            if (position[0] + position[1]) < 4:
                return ('white', '#ffb0b0')
            elif (position[0] + position[1] > 14):
                return ('white', '#99f3bd')
            else :
                return ('white', '#e7dec8')
        else :
            if (position[0] + position[1]) < 4:
                return ('white', '#ec0101')
            elif (position[0] + position[1] > 14):
                return ('white', '#28df99')
            else :
                return ('white', '#cbaf87')

    def generate_reverse_button_color(self, position):
        if (position[0] + position[1]) % 2 == 0:
            if (position[0] + position[1]) > 14:
                return ('white', '#ffb0b0')
            elif (position[0] + position[1]) < 4:
                return ('white', '#99f3bd')
            else :
                return ('white', '#e7dec8')
        else :
            if (position[0] + position[1]) > 14:
                return ('white', '#ec0101')
            elif (position[0] + position[1]) < 4:
                return ('white', '#28df99')
            else :
                return ('white', '#cbaf87')

    def render(self, board):
        for i in range(board.b_size):
            for j in range(board.b_size):
                for pawn in board.pawns:
                    if pawn.position.location == (i,j):
                        self.window[(i,j)].update(str(pawn))
        self.window.read(timeout=100)

    def render_color_reverse(self):
        for i in range(constant):
            for j in range(constant):
                if self.reverse :
                    self.window[(i,j)].update("", button_color=self.generate_reverse_button_color((i,j)))
                else:
                    self.window[(i,j)].update("", button_color=self.generate_button_color((i,j)))
        
        self.reverse = not self.reverse
        self.window.read(timeout=100)
        


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
