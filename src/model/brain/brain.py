from abc import ABCMeta, abstractmethod

class Brain(metaclass=ABCMeta):
    '''Base class of brain for the AI implemented in Halma Game
    '''
    @abstractmethod
    def find_best_move(self, utility_function, state):
        raise NotImplementedError
    