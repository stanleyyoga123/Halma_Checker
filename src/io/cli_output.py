from clint.textui import puts, colored

from src.model.board import Board

class CLIOutput():
    def show(self, board):
        print(colored.green(board))