import Puzzle


class ManhattanDistance:
    def __init__(self, puzzle: Puzzle):
        # Init with a Puzzle instance
        self.puzzle = puzzle

    def calculate(self, gameBoard):
        """
        Calculate the Manhattan distance:
        The sum of the distances of all fields from their target position.
        """
        cost = 0

        for rowIndex in range(3):
            for colIndex in range(3):
                tile = gameBoard[rowIndex][colIndex]

                if tile != 0:  # ignore empty position
                    # calculate target position
                    targetRow = tile // 3
                    targetCol = tile % 3

                    # sum Manhattan distance
                    cost += abs(rowIndex - targetRow) + abs(colIndex - targetCol)

        return cost


class HammingDistance:
    def __init__(self, puzzle: Puzzle):
        # Init with a Puzzle instance
        self.puzzle = puzzle

    def calculate(self, gameBoard):
        """
        Calculate the Hamming distance:
        The number of fields that are not at the target position.
        """
        cost = 0

        for rowIndex in range(3):
            for colIndex in range(3):
                currentTile = gameBoard[rowIndex][colIndex]

                if currentTile != 0:  # ignore empty position
                    # check if the current position is correct
                    if currentTile != self.puzzle.goalState[rowIndex][colIndex]:
                        cost += 1

        return cost