from .model import Color

class Constant():
    '''Class for general constant that can be used on all class
    '''
    NOBRAIN="nobrain"
    MINIMAX="minimax"
    MINMAXWLOCAL="minimax + local search"

    BOARDSIZE=10

    PLAYER1=Color.RED
    PLAYER2=Color.GREEN

    # Color constant
    LIGHTRED="#ffb0b0"
    DARKRED="#ec0101"
    PAWNRED="#7d0633"
    POSSIBLERED="#f57b51"

    LIGHTGREEN="#99f3bd"
    DARKGREEN="#28df99"
    PAWNGREEN="#065446"
    POSSIBLEGREEN="#ffd571"

    LIGHTBOARD="#e7dec8"
    DARKBOARD="#cbaf87"
    SIZE=6 # in 1080(windows) -> 3 | in 720 (linux) -> 6

    PAWNCHAR="♟"
    TARGETCHAR="X"

    PAWNREDTYPE="R"
    PAWNGREENTYPE="G"