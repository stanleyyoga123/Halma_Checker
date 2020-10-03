import PySimpleGUI as sg
sg.theme('DarkAmber')
constant = 10

class GUI():
    def __init__(self):
        board = [[(i,j) for j in range(constant)] for i in range(constant)]
        layout = [
            [sg.B('', size=(4, 2), key=(i,j), pad=(0,0), button_color=('white','black')) if (i+j) % 2 == 0 else sg.B('', size=(4, 2), key=(i,j), pad=(0,0), button_color=('white','yellow'))
              for j in range(constant)] for i in range(constant)]
        self.window = sg.Window('Halma Checker', layout)

    


if __name__ == '__main__':
    gui = GUI()
    while True: 
        event, values = gui.window.read()
        if (type(event) == tuple):
            print(event)
        if event in (None, 'Exit'):
            gui.window.close()
            break
