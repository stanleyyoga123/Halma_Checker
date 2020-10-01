from src.halma import Halma
from src.model import Color, Pawn, Tile
from src.io import CLIInput, CLIOutput

if __name__ == '__main__':
    inputter = CLIInput()
    outputter = CLIOutput()
    game = Halma(10, 10, Color.RED, inputter, outputter)
    game.outputter.show(game.board)

    while True:
        game.game()