from ...constant import Constant

def translate_type(type):
    return {
        Constant.NOBRAIN : "Human",
        Constant.MINIMAX : "Bot with Minimax",
        Constant.MINMAXWLOCAL : "Minimax + Local Search"
    }.get(type)