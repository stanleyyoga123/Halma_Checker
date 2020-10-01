from src.model.board import Board
from src.model.player import Player 

class CLIInput():
    def input(self, board, player):
        print('List Pawns')
        for i, pawn in enumerate(player.pawns):
            print(f'{i+1}. Pawns at {pawn.position}')
        print()
        
        i_choosed_pawn = int(input('Choose Pawn: '))
        choosed_pawn = player.pawns[i_choosed_pawn-1]
        print(f'You Choose Pawn at {choosed_pawn.position}')
        print()

        print('Pawn Possible Moves:')
        possible_moves = board.possible_moves(choosed_pawn)
        
        for i, pawn in enumerate(possible_moves):
            print(f'{i+1}. Pawn to {pawn.position}')
        print()

        i_moved_pawn = int(input('Choose Movement: '))
        moved_pawn = possible_moves[i_moved_pawn-1] 
        print(f'You Choose Pawn from {choosed_pawn.position} Move to {moved_pawn.position}')
        print()

        return (choosed_pawn, moved_pawn)