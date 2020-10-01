from src.model.board import Board
from src.model.player import Player 

class CLIInput():
    def input(self, board, player):
        print('List Pawns')
        for i, pawn in enumerate(player.pawns):
            print(f'{i+1}. Pawns at {pawn.position}')
        
        choosed_pawn = int(input('Choose Pawn: '))
        pawn = player.pawns[choosed_pawn-1]
        print(f'You Choose Pawn at {pawn.position}')

        print('Pawn Possible Moves:')
        possible_moves = board.possible_moves(pawn)
        
        for i, pawn in enumerate(possible_moves):
            print(f'{i+1}. Pawns to {pawn.position}')