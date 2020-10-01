from src.halma import Halma
from src.model import Color
from src.model import Pawn
from src.model import Tile

if __name__ == '__main__':
    game = Halma(10, 10, Color.RED)
    print(game.board)

    while True:
        game.game()