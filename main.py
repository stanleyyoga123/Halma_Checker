import sys
import time

from src.halma import Halma
from src.model import Color, Pawn, Tile
from src.constant import Constant
from src.io import CLI, GUI

if __name__ == '__main__': 
	CLI().show_title()

	# Initialize game settings
	settings = CLI().ask_game_settings()
	player1, player2 = settings.get('mode')
	interface_type = settings.get('interface')
	time_limit = settings.get('time')
	board_size = settings.get('size')
	pcolor = settings.get('pcolor') if settings.get('pcolor') is not None else Color.RED # only change for player color
	interface = GUI(board_size) if interface_type == 'gui' else CLI()

	if interface_type == 'gui':
		interface.init_loading_screen() #-> open only for loading screen
		interface.init_game_board()

	# Start the game
	game = Halma(board_size, time_limit, pcolor, interface, player1=player1, player2=player2)
	game.interface.render(game.state)

	while True:
		try:
			game.game()
		except RuntimeError:
			print('Exit Game!')
			break

		if game.game_over :
			print("Game end, winner: ", game.state.currentPlayer)
			break 