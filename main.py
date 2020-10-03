import sys
import time

from src.halma import Halma
from src.model import Color, Pawn, Tile
from src.constant import Constant
from src.io import CLI, GUI

	
if __name__ == '__main__':
	cli = CLI()
	cli.show_title()
	player1, player2 = cli.ask_game_mode()

	interface_type = cli.select_interface()
	interface = GUI() if interface_type == 'gui' else CLI()

	game = Halma(Constant.BOARDSIZE, Constant.BOARDSIZE, Color.RED, interface, player1=player1, player2=player2)
	game.interface.render(game.state)

	try :
		while True:
			game.game()
	except Exception as err:
		CLI().show_ending(ending="Game Ended!")
		sys.exit(1)
	
