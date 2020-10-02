class Utility():
    '''Class for general function that can be used on all class
    '''
    @staticmethod
    def distance(coordinate, destination):
        '''Given two point, find the euclidean distance

        Parameters:
            coordinate (tuple(int, int)): Given Point
            destination (tuple(int, int)): Destination
        
        Returns:
            int: Euclidean Distance
        '''
        euclidean = 0
        for d_coordinate, d_destination in zip(coordinate, destination):
            euclidean += (d_coordinate - d_destination) ** 2
        euclidean = euclidean ** (0.5)

        return euclidean