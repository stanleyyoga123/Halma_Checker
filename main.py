import sys

from src.halma import Halma
from src.model import Color, Pawn, Tile
from src.constant import Constant
from src.io import CLI, GUI

	
if __name__ == '__main__':
	interface = CLI()
	interface.show_title()
	player1, player2 = interface.ask_game_mode()
	game = Halma(Constant.BOARDSIZE, Constant.BOARDSIZE, Color.RED, interface, player1=player1, player2=player2)
	game.interface.render(game.state.board)

	# TODO : create a loop for event GUI 
	try :
		while True:
			game.game()
	except Exception as err:
		CLIPrompt().show_ending(ending="Game Ended!")
		sys.exit(1)
	
