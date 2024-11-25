import random


class puzzle:
    # define goalstate
    goalState = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]]  # 0 is blank tile on top left

    def __init__(self, gameBoard=None):
        """Initialize the puzzle with a gameboard. If no gameboard is provided, create one."""
        self.gameBoard = gameBoard
        if self.gameBoard is None:
            self.createRandomGameBoard()

    def createRandomGameBoard(self):
        """Create a random gameboard that is solvable."""
        while True:  # Repeat until a solvable board is generated
            # Create a random list of numbers from 0 to 8
            #numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            #random.shuffle(numbers)
            numbers = [4,1,2,0,9,6,7,5,8]

            # Fill the gameboard with the random numbers
            self.gameBoard = []  # Initialize an empty list for the game board
            for i in range(0, len(numbers), 3):  # Loop through indices in steps of 3
                row = numbers[i:i + 3]  # Take a slice of 3 elements from the list
                self.gameBoard.append(row)  # Append the slice as a row to the game board

            # Check if the random gameboard is solvable
            if self.is_solvable():
                break

    def printGameBoard(self):
        """Print the current state of the gameboard in a readable format."""
        for row in self.gameBoard:
            print(row)

    # is solvable

    def is_solvable(self):

        inversions = 0
        flattenedPuzzle = []
        for row in self.gameBoard:  # Loop through each row in the gameboard
            for tile in row:  # Loop through each tile in the row
                if tile != 0:  # Check if the tile is not 0
                    flattenedPuzzle.append(tile)  # Add the tile to the flattened_puzzle list

        for i in range(len(flattenedPuzzle)):
            for j in range(i + 1, len(flattenedPuzzle)):
                if flattenedPuzzle[i] > flattenedPuzzle[j]:
                    inversions += 1

        # check if even number
        if len(self.gameBoard) % 2 != 0:
            return inversions % 2 == 0
        else:
            blank_row = next(row for row, tiles in enumerate(self.gameBoard)
                             if 0 in tiles)
            return (blank_row % 2 == 0) == (inversions % 2 != 0)
