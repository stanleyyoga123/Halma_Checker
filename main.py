from src.halma import Halma
from src.model import Color, Pawn, Tile
from src.io import CLIInput, CLIOutput, CLIOpening
	
if __name__ == '__main__':
	CLIOpening().show_title()
	game_mode = CLIOpening().ask_game_mode()

	inputter = CLIInput()
	outputter = CLIOutput()
	game = Halma(10, 10, Color.RED, inputter, outputter)
	game.outputter.show(game.board)

	while True:
		game.game()