import sys

from src.halma import Halma
from src.model import Color, Pawn, Tile
from src.constant import Constant
from src.io import CLIInput, CLIOutput, CLIPrompt

	
if __name__ == '__main__':
	CLIPrompt().show_title()
	player1, player2 = CLIPrompt().ask_game_mode()

	inputter = CLIInput()
	outputter = CLIOutput()
	game = Halma(Constant.BOARDSIZE, Constant.BOARDSIZE, Color.RED, inputter, outputter, player1=player1, player2=player2)
	game.outputter.show(game.state.board)

	# TODO : create a loop for event GUI 
	try :
		while True:
			game.game()
	except Exception as err:
		CLIPrompt().show_ending(ending="Game Ended!")
		sys.exit(1)
	
